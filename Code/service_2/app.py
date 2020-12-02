from flask import Flask, Response, request, jsonify
import random

app = Flask(__name__)

@app.route('/city', methods=['GET'])
def city():
    cities = ["London", "Paris", "New York", "Tokyo", "Istanbul", "Rome", "Los Angeles", "Hong Kong", "Amsterdam", "Berlin"]
    return Response(random.choices(cities), mimetype="text/plain")

if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)

