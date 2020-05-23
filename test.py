import unittest

from app import app


class TestCases(unittest.TestCase):

    def test_text(self):
        """Assert that the click button works and returns text."""
        app.debug = True
		self.test_app = app.test_client()
        response = app.test_client().get('/click')
		self.assertIn('text_', response.data)
        self.assertEquals(response.status_code, 200)
