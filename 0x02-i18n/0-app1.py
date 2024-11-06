#!/usr/bin/env python3
"""A basic flask app"""
from flask import Flask, render_template


App = Flask(__name__)


@App.route('/')
def home():
    """home route"""
    return render_template('0-index.html')


if __name__ == "__main__":
    App.run(debug=True, host='127.0.0.1', port=5000)
