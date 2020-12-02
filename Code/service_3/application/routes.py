from flask import Flask, Response, request
import random
from application import app

@app.route('/weather', methods=['GET'])
def weather():
    weather_conditions: ["rain", "sun", "snow", "wind", "cloud"]
    return Response(random.choices(weather_conditions), mimetype="text/plain")

