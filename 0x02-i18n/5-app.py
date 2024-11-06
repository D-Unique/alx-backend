#!/usr/bin/env python3
"""A basic flask app"""
from flask import Flask, render_template, request, g, url_for
from flask_babel import Babel
from typing import Dict


class Config:
    """configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = "en"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user() -> Dict:
    """get user"""
    if (request.args.get('login_as') in users.keys()):
        return  users['login_as'] 
    return None

@app.before_request
def before_request():
   """first run"""
   g.user = get_user()
  
   if g.user is None:
       login = "You are not logged in."
       return url_for(home, login=login)
   login = f"You are logged in as {g.user.name}."
   return url_for(home, login=login)


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

    return render_template('3-index.html', title=title, greet=greet)


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
