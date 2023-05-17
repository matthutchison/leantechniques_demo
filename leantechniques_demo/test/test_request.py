from leantechniques_demo.request import get_photos
import requests
from unittest import TestCase
from unittest.mock import patch

class RequestTestCase(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @patch.object(requests, 'get')
    def test_request_called_with_good_values(self, mock):
        get_photos(id='1', albumId='1')
        self.assertTrue(mock.called)

    @patch.object(requests, 'get')
    def test_request_raises_with_bad_id(self, mock):
        with self.assertRaises(ValueError):
            get_photos(id='bad')
        self.assertFalse(mock.called)
        with self.assertRaises(ValueError):
            get_photos(id='bad', albumId='1')
        self.assertFalse(mock.called)
        with self.assertRaises(ValueError):
            get_photos(id='1.1', albumId='1')
        self.assertFalse(mock.called)
        with self.assertRaises(ValueError):
            get_photos(id=' ', albumId='1')
        self.assertFalse(mock.called)

    @patch.object(requests, 'get')
    def test_request_raises_with_bad_albumId(self, mock):
        with self.assertRaises(ValueError):
            get_photos(albumId='bad')
        self.assertFalse(mock.called)
        with self.assertRaises(ValueError):
            get_photos(id='1', albumId='bad')
        self.assertFalse(mock.called)
        with self.assertRaises(ValueError):
            get_photos(id='1', albumId='1.1')
        self.assertFalse(mock.called)
        with self.assertRaises(ValueError):
            get_photos(id='1', albumId=' ')
        self.assertFalse(mock.called)
