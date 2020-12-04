from flask import Flask, Response, request
import random
from application import app

@app.route('/suggestion', methods=['POST'])
def suggestion():
    weather = request.data.decode('utf-8')
    if weather == "rain":
        suggestion = "Not a great time to visit"
    elif weather == "sun":
        suggestion = "It is a great time to visit"
    elif weather == "snow":
        suggestion = "Wrap up warm"
    elif weather == "wind":
        suggestion = "It could get a little brisk"
    elif weather == "cloud":
        suggestion = "It's a bit dull, but at least it isn't raining"
    else:
        suggestion = "No suggestion available"
    return Response(suggestion, mimetype="text/plain")

