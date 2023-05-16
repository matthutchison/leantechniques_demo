from leantechniques_demo.data import Album
from unittest import TestCase

class DataTestCase(TestCase):
    '''Tests for the data repository object'''
    def setUp(self):
        self.default_album = Album(1, 1, 'title', 'https://example.com/url', 'https://example.com/thumbnailUrl')

    def tearDown(self):
        del self.default_album

    def test_validation_succeeds_on_good_values(self):
        self.assertTrue(self.default_album.validate())

    def test_validation_raises_on_bad_albumId(self):
        with self.assertRaises(TypeError):
            self.default_album.albumId = 'bad'
            self.default_album.validate()

    def test_validation_raises_on_bad_id(self):
        with self.assertRaises(TypeError):
            self.default_album.id = 'bad'
            self.default_album.validate()

    def test_validation_raises_on_bad_url(self):
        with self.assertRaises(ValueError):
            self.default_album.url = 'bad'
            self.default_album.validate()
        with self.assertRaises(ValueError):
            self.default_album.url = 'https:/bad.com'
            self.default_album.validate()
        with self.assertRaises(ValueError):
            self.default_album.url = 'https://'
            self.default_album.validate()

    def test_validation_raises_on_bad_thumbnailUrl(self):
        with self.assertRaises(ValueError):
            self.default_album.thumbnailUrl = 'bad'
            self.default_album.validate()
        with self.assertRaises(ValueError):
            self.default_album.thumbnailUrl = 'https:/bad.com'
            self.default_album.validate()
        with self.assertRaises(ValueError):
            self.default_album.thumbnailUrl = 'https://'
            self.default_album.validate()