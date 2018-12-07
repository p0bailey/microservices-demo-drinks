"""
This file demonstrates common uses for the Python unittest module with Flask

Documentation:

* https://docs.python.org/3/library/unittest.html
* http://flask.pocoo.org/docs/latest/testing/
"""
import unittest

from app import app

class TestPost(unittest.TestCase):


    def test_post_root(self):
        self.test_app = app.test_client()
        response = self.test_app.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_post_host(self):
        self.test_app = app.test_client()
        response = self.test_app.get('/hostname')
        self.assertEqual(response.status_code, 200)
        assert b"This app is served from" in response.data

    def test_post_api(self):
        self.test_app = app.test_client()
        response = self.test_app.get('/beer/1')
        self.assertEqual(response.status_code, 200)
        assert b"1" in response.data

if __name__ == '__main__':
    unittest.main()
