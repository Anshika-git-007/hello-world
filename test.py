import unittest

from betamax import Betamax
from app import app

with Betamax.configure() as config:
    config.cassette_library_dir = 'test/fixtures'

test_auth_token = 'MLth87eHvSAaCQ1vn7jTd0xA9Kapo5'


class TestCases(unittest.TestCase):

    def test_root_endpoint(self):
        """Assert that the / endpoint correctly redirects to web app."""
        response = app.test_client().get('/')
        self.assertIn('login.uber.com', response.data)
