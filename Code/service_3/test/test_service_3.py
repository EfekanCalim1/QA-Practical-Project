from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests

from application import app



class TestBase(TestCase):
    def create_app(self):
        return app 

class TestResponse(TestBase):
    def test_weather(self):
        response = self.client.get(url_for('weather'))
        self.assertEqual(response.status_code, 200)
     