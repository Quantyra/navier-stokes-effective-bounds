"""Mocked API checks: complete upload, idempotent retry, conflicts, wrong target."""
import tempfile
import unittest
from pathlib import Path
from figshare_upload import API, ITEM, checksum, upload, validate_item


class FakeClient:
    def __init__(self, path, existing=None, bad_digest=False):
        self.path = path
        self.existing = existing or []
        self.written = b''
        self.bad_digest = bad_digest
        self.created = 0

    def request(self, method, endpoint, data=None, binary=False):
        location = API + ITEM + '/files/42'
        if method == 'GET' and endpoint == ITEM:
            return {'files': self.existing}
        if method == 'POST' and endpoint == ITEM + '/files':
            self.created += 1
            return {'location': location}
        if method == 'GET' and endpoint == location:
            return {'id': 42, 'upload_url': 'https://uploads.figshare.com/upload/test',
                    'computed_md5': 'wrong' if self.bad_digest else checksum(self.path),
                    'size': self.path.stat().st_size}
        if method == 'GET' and endpoint.endswith('/upload/test'):
            return {'parts': [{'partNo': 1, 'startOffset': 0,
                               'endOffset': self.path.stat().st_size - 1}]}
        if method == 'PUT':
            self.written += data
            return None
        if method == 'POST' and endpoint == location:
            return None
        raise AssertionError((method, endpoint))


class UploadTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / 'sample.pdf'
        self.path.write_bytes(b'publication artifact')

    def test_upload(self):
        c = FakeClient(self.path)
        upload(c, self.path)
        self.assertEqual(c.written, self.path.read_bytes())

    def test_retry_skips_identical(self):
        c = FakeClient(self.path, [{'name': self.path.name, 'size': self.path.stat().st_size,
                                  'computed_md5': checksum(self.path)}])
        upload(c, self.path)
        self.assertEqual(c.created, 0)

    def test_conflict_stops(self):
        with self.assertRaises(RuntimeError):
            upload(FakeClient(self.path, [{'name': self.path.name}]), self.path)

    def test_bad_checksum_stops(self):
        with self.assertRaises(RuntimeError):
            upload(FakeClient(self.path, bad_digest=True), self.path)

    def test_wrong_item_stops(self):
        with self.assertRaises(RuntimeError):
            validate_item({'id': 1, 'title': 'right', 'license': {'value': 7}}, 'right')


if __name__ == '__main__':
    unittest.main()
