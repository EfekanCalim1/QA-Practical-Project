from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestLondon(TestBase):
    def test_suggestion_sun(self):
        with patch("requests.get") as i:
            i.return_value.text = 'London'
            with patch("random.choices") as r:
                r.return_value = 'sun'
                response = self.client.post(
                url_for('suggestion'),
                data = 'sun London')
                self.assertIn(b'No suggestion available', response.data)

class TestTokyo(TestBase):
    def test_suggestion_rain(self):
        with patch("requests.get") as i:
            i.return_value.text = 'Tokyo'
            with patch("random.choices") as r:
                r.return_value = 'rain'
                response = self.client.post(
                url_for('suggestion'),
                data = 'rain Tokyo')
                self.assertIn(b'No suggestion available', response.data)

class TestNewYork(TestBase):
    def test_suggestion_snow(self):
        with patch("requests.get") as i:
            i.return_value.text = 'New York'
            with patch("random.choices") as r:
                r.return_value = 'sun'
                response = self.client.post(
                url_for('suggestion'),
                data = 'snow New York')
                self.assertIn(b'No suggestion available', response.data)

class TestIstanbul(TestBase):
    def test_suggestion_cloud(self):
        with patch("requests.get") as i:
            i.return_value.text = 'Istanbul'
            with patch("random.choices") as r:
                r.return_value = 'cloud'
                response = self.client.post(
                url_for('suggestion'),
                data = 'cloud Istanbul')
                self.assertIn(b'No suggestion available', response.data)

class TestAmsterdam(TestBase):
    def test_suggestion_wind(self):
        with patch("requests.get") as i:
            i.return_value.text = 'Amsterdam'
            with patch("random.choices") as r:
                r.return_value = 'wind'
                response = self.client.post(
                url_for('suggestion'),
                data = 'wind Amsterdam')
                self.assertIn(b'No suggestion available', response.data)

class TestRome(TestBase):
    def test_suggestion_sun(self):
        with patch("requests.get") as i:
            i.return_value.text = 'Rome'
            with patch("random.choices") as r:
                r.return_value = 'sun'
                response = self.client.post(
                url_for('suggestion'),
                data = 'sun Rome')
                self.assertIn(b'No suggestion available', response.data)
    
      
