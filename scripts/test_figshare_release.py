"""Release orchestration tests using an in-memory Figshare service; no network."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from figshare_release import (ITEM, PUBLIC, REPO, checksum, marker_name,
                              publish_release, release_context)


def entry(path, identifier=10):
    return {'id': identifier, 'name': path.name, 'size': path.stat().st_size,
            'computed_md5': checksum(path), 'supplied_md5': checksum(path),
            'is_link_only': False, 'download_url': 'https://example.invalid/file'}


class Service:
    def __init__(self):
        self.public = {'id': 33472651, 'title': 'Expected', 'license': {'value': 7},
                       'description': 'Conditional note', 'authors': [], 'files': [],
                       'version': 2, 'doi': '10.6084/m9.figshare.33472651.v2'}
        self.draft = copy.deepcopy(self.public)
        self.versions = [copy.deepcopy(self.public)]
        self.publishes = 0
        self.calls = []

    def request(self, method, path, data=None):
        self.calls.append((method, path))
        if method == 'GET' and path == PUBLIC + '/versions':
            return [{'version': v['version']} for v in self.versions]
        if method == 'GET' and path.startswith(PUBLIC + '/versions/'):
            return copy.deepcopy(next(v for v in self.versions if v['version'] == int(path.rsplit('/', 1)[1])))
        if method == 'GET' and path in (PUBLIC, ITEM):
            return copy.deepcopy(self.public if path == PUBLIC else self.draft)
        if method == 'DELETE':
            identifier = int(path.rsplit('/', 1)[1])
            self.draft['files'] = [f for f in self.draft['files'] if f['id'] != identifier]
            return None
        if method == 'POST' and path == ITEM + '/publish':
            self.publishes += 1
            self.draft['version'] = self.public['version'] + 1
            self.draft['doi'] = f"10.6084/m9.figshare.33472651.v{self.draft['version']}"
            self.public = copy.deepcopy(self.draft)
            self.versions.append(copy.deepcopy(self.public))
            return None
        raise AssertionError((method, path))

    def upload(self, client, path):
        self.draft['files'] = [f for f in self.draft['files'] if f['name'] != path.name]
        self.draft['files'].append(entry(path, max([f['id'] for f in self.draft['files']] + [10]) + 1))


class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.context = {'repository': REPO, 'release_id': 123, 'tag': 'v0.2.0', 'commit': 'a' * 40}
        self.paths = (self.root / 'effective-bounds.pdf',
                      self.root / ('navier-stokes-effective-bounds-' + 'a' * 40 + '.zip'),
                      self.root / marker_name(self.context))
        for p in self.paths[:2]:
            p.write_bytes(b'new release bytes')
        self.paths[2].write_text(json.dumps(self.context), encoding='utf-8')
        self.service = Service()
        self.patch = patch('figshare_release.upload', side_effect=self.service.upload)
        self.patch.start()
        self.addCleanup(self.patch.stop)

    def run_release(self):
        return publish_release(self.service, self.context, self.paths, 'Expected')

    def test_publish_and_retry_get_same_doi(self):
        first = self.run_release()
        second = self.run_release()
        self.assertEqual(first['doi'], second['doi'])
        self.assertEqual(self.service.publishes, 1)
        self.assertEqual(len(self.service.public['files']), 3)

    def test_changed_pdf_replaces_draft_preserves_history(self):
        old = entry(self.paths[0], 99)
        old['computed_md5'] = old['supplied_md5'] = 'oldhash'
        self.service.draft['files'] = [old]
        self.service.public['files'] = copy.deepcopy([old])
        self.service.versions[0] = copy.deepcopy(self.service.public)
        self.run_release()
        self.assertEqual(self.service.versions[0]['files'][0]['computed_md5'], 'oldhash')
        self.assertEqual(self.service.public['files'][0]['computed_md5'], checksum(self.paths[0]))

    def test_manual_metadata_changes_block_publication(self):
        self.service.draft['description'] = 'Unrelated unpublished edit'
        with self.assertRaisesRegex(RuntimeError, 'metadata edits'):
            self.run_release()
        self.assertFalse(any(method != 'GET' for method, _ in self.service.calls))

    def test_unknown_files_block_mutation(self):
        self.service.draft['files'] = [{'name': 'unrelated-results.csv'}]
        with self.assertRaisesRegex(RuntimeError, 'Unexpected draft files'):
            self.run_release()
        self.assertEqual(self.service.publishes, 0)

    def test_upload_failure_never_publishes(self):
        with patch('figshare_release.upload', side_effect=RuntimeError('upload failed')):
            with self.assertRaisesRegex(RuntimeError, 'upload failed'):
                self.run_release()
        self.assertEqual(self.service.publishes, 0)

    def test_historical_release_retry_does_not_publish_again(self):
        first = self.run_release()
        self.service.public = {**copy.deepcopy(self.service.public), 'version': 4, 'files': []}
        self.service.versions.append(copy.deepcopy(self.service.public))
        result = self.run_release()
        self.assertEqual(first['doi'], result['doi'])
        self.assertEqual(self.service.publishes, 1)

    def test_retargeted_release_is_rejected(self):
        self.run_release()
        self.context['commit'] = 'b' * 40
        with self.assertRaisesRegex(RuntimeError, 'different commit'):
            self.run_release()

    def test_event_gate(self):
        event = {'action': 'published', 'repository': {'full_name': REPO},
                 'release': {'id': 123, 'tag_name': 'v0.2.0', 'draft': False}}
        self.assertEqual(release_context(event, 'a' * 40)['release_id'], 123)
        event['action'] = 'edited'
        with self.assertRaises(RuntimeError):
            release_context(event, 'a' * 40)
        event['action'] = 'published'
        event['release']['draft'] = True
        with self.assertRaises(RuntimeError):
            release_context(event, 'a' * 40)


if __name__ == '__main__':
    unittest.main()
