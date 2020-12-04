from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_city(self):
        with patch("requests.get") as g:
            with patch("requests.post") as p:
                g.return_value.text = "sun"
                p.return_value.text = "It is a great time to visit"
                response = self.client.get(url_for('index'))
                self.assertIn(b'It is a great time to visit', response.data)