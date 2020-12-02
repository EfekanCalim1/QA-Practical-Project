from flask import Flask, Response, request
import random
from application import app

@app.route('/city', methods=['GET'])
def city():
    cities = ["London", "Paris", "New York", "Tokyo", "Istanbul", "Rome", "Los Angeles", "Hong Kong", "Amsterdam", "Berlin"]
    return Response(random.choices(cities), mimetype="text/plain")