from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestCity(TestBase):
    def test_city(self):
        cities = [b"London", b"Paris", b"New York", b"Tokyo", b"Istanbul", b"Rome", b"Los Angeles", b"Hong Kong", b"Amsterdam", b"Berlin"]
        response = self.client.get(url_for('city'))
        self.assertIn(response.data, cities)
