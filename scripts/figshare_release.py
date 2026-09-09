"""Archive a published GitHub release as one Figshare version, safely retryable."""
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess

from figshare_upload import API, Client, ITEM, ROOT, checksum, upload, validate_item

PUBLIC = '/articles/33472651'
REPO = 'Quantyra/navier-stokes-effective-bounds'


def release_context(event, revision):
    release = event.get('release', {})
    if (event.get('action') != 'published' or release.get('draft')
            or event.get('repository', {}).get('full_name') != REPO
            or not isinstance(release.get('id'), int)
            or not release.get('tag_name') or not re.fullmatch('[0-9a-f]{40}', revision)):
        raise RuntimeError('Expected a published release from the configured repository')
    return {'repository': REPO, 'release_id': release['id'],
            'tag': release['tag_name'], 'commit': revision}


def marker_name(context):
    return f"github-release-{context['release_id']}-{context['commit']}.json"


def managed(name):
    return (name == 'effective-bounds.pdf'
            or re.fullmatch(r'navier-stokes-effective-bounds-[0-9a-f]{12,40}\.zip', name)
            or re.fullmatch(r'github-release-[0-9]+-[0-9a-f]{40}\.json', name))


def metadata_signature(record):
    # Refuse to publish unrelated metadata edits staged through the website.
    fields = ('title', 'description', 'tags', 'references', 'funding', 'custom_fields')
    result = {k: record.get(k) for k in fields}
    result['authors'] = [(a.get('id'), a.get('full_name')) for a in record.get('authors', [])]
    result['license'] = record.get('license', {}).get('value')
    return result


def verify_files(record, paths):
    files = record['files']
    if len(files) != len(paths) or {f['name'] for f in files} != {p.name for p in paths}:
        raise RuntimeError('Figshare file inventory does not match the release bundle')
    expected = {p.name: p for p in paths}
    for f in files:
        p = expected[f['name']]
        if (f.get('is_link_only') or f.get('computed_md5') != checksum(p)
                or f.get('size') != p.stat().st_size):
            raise RuntimeError('Figshare file checksum/size verification failed')


def receipt(record, context):
    if not record.get('doi') or not record.get('version'):
        raise RuntimeError('Figshare has not returned a published version DOI')
    return {**context, 'doi': record['doi'], 'figshare_version': record['version'],
            'stable_doi': '10.6084/m9.figshare.33472651',
            'files': [{k: f.get(k) for k in ('name', 'size', 'computed_md5', 'download_url')}
                      for f in record['files']]}


def publish_release(client, context, paths, title):
    marker = marker_name(context)
    # Search historical versions too: rerunning an older release must not republish it.
    versions = client.request('GET', PUBLIC + '/versions')
    for entry in sorted(versions, key=lambda v: v['version'], reverse=True):
        record = client.request('GET', PUBLIC + '/versions/' + str(entry['version']))
        validate_item(record, title)
        for f in record['files']:
            if f['name'].startswith(f"github-release-{context['release_id']}-"):
                if f['name'] != marker:
                    raise RuntimeError('This GitHub release was already archived at a different commit')
                marker_path = next(p for p in paths if p.name == marker)
                if f.get('computed_md5') != checksum(marker_path):
                    raise RuntimeError('Published release marker does not match the release identity')
                return receipt(record, context)

    public = client.request('GET', PUBLIC)
    draft = client.request('GET', ITEM)
    validate_item(public, title)
    validate_item(draft, title)
    if metadata_signature(public) != metadata_signature(draft):
        raise RuntimeError('Figshare has unrelated draft metadata edits; resolve those before release')
    if any(not managed(f['name']) or f.get('is_link_only') for f in draft['files']):
        raise RuntimeError('Unexpected draft files; refusing automatic replacement')
    expected = {p.name: p for p in paths}
    for f in draft['files']:
        if f['name'] in expected and f.get('computed_md5') != checksum(expected[f['name']]):
            # Preserve an identical partial upload for the upload client's resume logic.
            p = expected[f['name']]
            if f.get('supplied_md5') == checksum(p) and not f.get('computed_md5'):
                continue
            client.request('DELETE', ITEM + '/files/' + str(f['id']))
    for p in paths:
        upload(client, p)
    # Keep only this release's bundle in the draft; published historical versions remain intact.
    for f in client.request('GET', ITEM)['files']:
        if f['name'] not in expected:
            if not managed(f['name']):
                raise RuntimeError('Unexpected file appeared during upload')
            client.request('DELETE', ITEM + '/files/' + str(f['id']))
    draft = client.request('GET', ITEM)
    if metadata_signature(public) != metadata_signature(draft):
        raise RuntimeError('Draft metadata changed during upload; not publishing')
    verify_files(draft, paths)
    client.request('POST', ITEM + '/publish')
    for _ in range(30):
        published = client.request('GET', PUBLIC)
        if any(f['name'] == marker for f in published['files']):
            verify_files(published, paths)
            return receipt(published, context)
    raise RuntimeError('Publication submitted but public verification is pending; rerun to recover')


def main():
    if os.environ.get('GITHUB_EVENT_NAME') != 'release':
        raise RuntimeError('Automatic publishing is restricted to GitHub release events')
    event = json.loads(Path(os.environ['GITHUB_EVENT_PATH']).read_text(encoding='utf-8'))
    revision = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    context = release_context(event, revision)
    tag_commit = subprocess.check_output(['git', 'rev-parse', '--verify',
                                         'refs/tags/' + context['tag'] + '^{commit}'],
                                        cwd=ROOT, text=True).strip()
    if revision != tag_commit:
        raise RuntimeError('Checkout does not match the release tag')
    token = os.environ.get('FIGSHARE_TOKEN', '').strip()
    if not token:
        raise RuntimeError('FIGSHARE_TOKEN secret is missing')
    bundle = ROOT / 'tmp/figshare-release'
    bundle.mkdir(parents=True, exist_ok=True)
    pdf = bundle / 'effective-bounds.pdf'
    shutil.copyfile(ROOT / 'output/pdf/effective-bounds.pdf', pdf)
    archive = bundle / f'navier-stokes-effective-bounds-{revision}.zip'
    subprocess.run(['git', 'archive', '--format=zip', '--prefix=navier-stokes-effective-bounds/',
                    '-o', str(archive), revision], cwd=ROOT, check=True)
    marker = bundle / marker_name(context)
    marker.write_text(json.dumps(context, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    title = json.loads((ROOT / '.zenodo.json').read_text(encoding='utf-8'))['title']
    result = publish_release(Client(token), context, (pdf, archive, marker), title)
    (bundle / 'figshare-receipt.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    message = f"Figshare DOI: https://doi.org/{result['doi']}\nSource commit: {revision}\n"
    print(message)
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a', encoding='utf-8') as out:
            out.write(message)


if __name__ == '__main__':
    try:
        main()
    except (RuntimeError, ValueError, KeyError) as exc:
        raise SystemExit(str(exc)) from None
