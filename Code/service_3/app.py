from flask import Flask, Response, request, jsonify
import random

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def weather():
    weather_conditions: ["rain", "sun", "snow", "wind", "cloud"]
    return Response(random.choices(weather_conditions), mimetype="text/plain")

if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)