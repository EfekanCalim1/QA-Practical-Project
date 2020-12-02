from flask import Flask, Response, request, jsonify
import random

app = Flask(__name__)

@app.route('/suggestion', methods=['POST'])
def suggestion():
    city