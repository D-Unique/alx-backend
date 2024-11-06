#!/usr/bin/env python3
"""A basic flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = "en"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """get locale"""
    if (request.args.get('locale') in Config.LANGUAGES):
        return request.args.get('locale')
    return request.accept_languages.best_match(['LANGUAGES'])


@app.route('/')
def home():
    """home route"""
    title = 'Welcome to Holberton'
    greet = 'Hello world'

    return render_template('4-index.html', title=title, greet=greet)


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
