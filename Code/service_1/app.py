from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    city = requests.get("http://localhost:5001/city")
    weather = requests.get("http://localhost:5002/weather")
    suggestion = requests.post("http://localhost:5003/suggestion", data=weather.text)

    return render_template('index.html', city=city.text, weather=weather.text, suggestion=suggestion.text)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')