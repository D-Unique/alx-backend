#!/usr/bin/env python3
"""A basic flask app"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = "en"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def home():
    """home route"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
