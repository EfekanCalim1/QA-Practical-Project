from flask import url_for
from flask_testing import TestCase

from app import app 

class TestBase(TestCase):
    def create_app(self):
        return app

class TestWeather(TestBase):
    def test_weather(self):
        weather_conditions = [b"rain", b"sun", b"snow", b"wind", b"cloud"]
        response = self.client.post(url_for('weather'))
        self.assertIn(response.data, weather_conditions)

    def test_suggestion_sun(self):
        response = self.client.post(
            url_for('weather'),
            data="sun",
            follow_redirects=True
        )
        self.assertIn(b'It is a great time to visit', response.data)
    
    def test_suggestion_rain(self):
        response = self.client.post(
            url_for('weather'),
            data="rain",
            follow_redirects=True
        )
        self.assertIn(b'Not a great time to visit', response.data)

    def test_suggestion_wind(self):
        response = self.client.post(
            url_for('weather'),
            data="wind",
            follow_redirects=True
        )
        self.assertIn(b'It could get a little brisk', response.data)

    def test_suggestion_cloud(self):
        response = self.client.post(
            url_for('weather'),
            data="cloud",
            follow_redirects=True
        )
        self.assertIn(b"It's a bit dull, but at least it isn't raining", response.data)
    
    def test_suggestion_snow(self):
        response = self.client.post(
            url_for('weather'),
            data="snow",
            follow_redirects=True
        )
        self.assertIn(b"Wrap up warm", response.data)
      
