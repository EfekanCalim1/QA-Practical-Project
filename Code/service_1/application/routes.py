from flask import Flask, render_template, request
import requests
from application import app

@app.route('/', methods=['GET']) 
def index():
    city = requests.get("http://service_2:5001/city")
    weather = requests.get("http://service_3:5002/weather")
    suggestion = requests.post("http://service_4:5003/suggestion", data=weather.text)

    return render_template('index.html', city=city.text, weather=weather.text, suggestion=suggestion.text)