"""Upload the PDF and a frozen git archive to one Figshare draft; never publish."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
API = 'https://api.figshare.com/v2'
ITEM = '/account/articles/33472651'


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class Client:
    def __init__(self, token):
        self.token = token
        self.opener = urllib.request.build_opener(NoRedirect)
        self.last_request = 0.0

    def request(self, method, path, data=None, binary=False):
        url = API + path if path.startswith('/') else path
        parsed = urllib.parse.urlsplit(url)
        if (parsed.scheme != 'https' or parsed.username or parsed.password
                or parsed.port not in (None, 443)
                or not (parsed.hostname == 'figshare.com'
                        or (parsed.hostname or '').endswith('.figshare.com'))):
            raise RuntimeError('Unexpected Figshare endpoint; no request sent')
        headers = {}
        if parsed.hostname == 'api.figshare.com':
            headers['Authorization'] = 'token ' + self.token
        if data is not None and not binary:
            data = json.dumps(data).encode()
            headers['Content-Type'] = 'application/json'
        elif binary:
            headers['Content-Type'] = 'application/octet-stream'
        time.sleep(max(0, 1.05 - (time.monotonic() - self.last_request)))
        self.last_request = time.monotonic()
        try:
            with self.opener.open(urllib.request.Request(
                    url, data=data, headers=headers, method=method), timeout=90) as response:
                payload = response.read()
        except urllib.error.HTTPError as exc:
            # Never echo response bodies or signed upload URLs into Actions logs.
            raise RuntimeError(f'Figshare request failed: HTTP {exc.code}') from None
        except urllib.error.URLError:
            raise RuntimeError('Figshare network request failed') from None
        return json.loads(payload) if payload and not binary else None


def checksum(path):
    return hashlib.md5(path.read_bytes()).hexdigest()


def validate_item(item, title):
    if item.get('title') != title or item.get('license', {}).get('value') != 7:
        raise RuntimeError('Figshare title/license does not match this publication')
    if int(item.get('id', 0)) != 33472651:
        raise RuntimeError('Unexpected Figshare item')


def upload(client, path):
    digest, size = checksum(path), path.stat().st_size
    files = client.request('GET', ITEM)['files']
    same = [f for f in files if f['name'] == path.name]
    if same:
        if len(same) == 1 and same[0].get('computed_md5') == digest and same[0]['size'] == size:
            print('Already verified:', path.name)
            return
        raise RuntimeError(f'Existing filename differs or is incomplete: {path.name}; inspect draft')
    result = client.request('POST', ITEM + '/files',
                            {'name': path.name, 'size': size, 'md5': digest})
    location = result['location']
    if not location.startswith(API + ITEM + '/files/'):
        raise RuntimeError('Unexpected file-creation response')
    info = client.request('GET', location)
    parts = client.request('GET', info['upload_url'])['parts']
    ordered = sorted(parts, key=lambda p: p['startOffset'])
    offset = 0
    with path.open('rb') as stream:
        for part in ordered:
            start, end = part['startOffset'], part['endOffset']
            if start != offset or not start <= end < size:
                raise RuntimeError('Invalid or incomplete upload part ranges')
            stream.seek(start)
            client.request('PUT', info['upload_url'] + '/' + str(part['partNo']),
                           stream.read(end - start + 1), binary=True)
            offset = end + 1
    if offset != size:
        raise RuntimeError('Upload parts do not cover the complete file')
    client.request('POST', location)
    for _ in range(12):
        final = client.request('GET', location)
        if final.get('computed_md5') == digest and final.get('size') == size:
            print('Uploaded and verified:', path.name)
            return
    raise RuntimeError(f'Uploaded file checksum not confirmed: {path.name}')


def main():
    token = os.environ.get('FIGSHARE_TOKEN', '').strip()
    if not token:
        raise RuntimeError('Add the FIGSHARE_TOKEN repository Actions secret first')
    client = Client(token)
    title = json.loads((ROOT / '.zenodo.json').read_text(encoding='utf-8'))['title']
    validate_item(client.request('GET', ITEM), title)
    revision = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    bundle = ROOT / 'tmp' / 'figshare'
    bundle.mkdir(parents=True, exist_ok=True)
    pdf = bundle / 'effective-bounds.pdf'
    shutil.copyfile(ROOT / 'output/pdf/effective-bounds.pdf', pdf)
    archive = bundle / f'navier-stokes-effective-bounds-{revision[:12]}.zip'
    subprocess.run(['git', 'archive', '--format=zip',
                    '--prefix=navier-stokes-effective-bounds/', '-o', str(archive), revision],
                   cwd=ROOT, check=True)
    for path in (pdf, archive):
        upload(client, path)
    summary = ('Figshare item 33472651: PDF and source ZIP verified in draft.\n'
               f'Source commit: {revision}\n'
               'No publication was performed. Publish the updated version in Figshare.\n')
    print(summary)
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a', encoding='utf-8') as out:
            out.write(summary)


if __name__ == '__main__':
    try:
        main()
    except (RuntimeError, ValueError, KeyError) as exc:
        raise SystemExit(str(exc)) from None
