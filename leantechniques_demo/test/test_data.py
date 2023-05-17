from leantechniques_demo.data import Photo
from unittest import TestCase

class DataTestCase(TestCase):
    '''Tests for the data repository object'''
    def setUp(self):
        self.default_photo = Photo(1, 1, 'title', 'https://example.com/url', 'https://example.com/thumbnailUrl')

    def tearDown(self):
        del self.default_photo

    def test_validation_succeeds_on_good_values(self):
        self.assertTrue(self.default_photo.validate())

    def test_validation_raises_on_bad_albumId(self):
        with self.assertRaises(TypeError):
            self.default_photo.albumId = 'bad'
            self.default_photo.validate()

    def test_validation_raises_on_bad_id(self):
        with self.assertRaises(TypeError):
            self.default_photo.id = 'bad'
            self.default_photo.validate()

    def test_validation_raises_on_bad_url(self):
        with self.assertRaises(ValueError):
            self.default_photo.url = 'bad'
            self.default_photo.validate()
        with self.assertRaises(ValueError):
            self.default_photo.url = 'https:/bad.com'
            self.default_photo.validate()
        with self.assertRaises(ValueError):
            self.default_photo.url = 'https://'
            self.default_photo.validate()

    def test_validation_raises_on_bad_thumbnailUrl(self):
        with self.assertRaises(ValueError):
            self.default_photo.thumbnailUrl = 'bad'
            self.default_photo.validate()
        with self.assertRaises(ValueError):
            self.default_photo.thumbnailUrl = 'https:/bad.com'
            self.default_photo.validate()
        with self.assertRaises(ValueError):
            self.default_photo.thumbnailUrl = 'https://'
            self.default_photo.validate()