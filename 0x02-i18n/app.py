#!/usr/bin/env python3
"""app.py - Display the current time """


from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from datetime import datetime
import pytz


app = Flask(__name__)
babel = Babel(app)


users = {
         1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
         2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
         3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
         4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
         }


class Config:
    """Locale configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """determine the best match supported languages."""
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    user = getattr(g, 'user', None)
    if user:
        return user['locale']
    if request.accept_languages:
        return request.accept_languages.best_match(app.config['LANGUAGES'])
    return Config.BABEL_DEFAULT_LOCALE


@babel.timezoneselector
def get_timezone() -> pytz.timezone:
    """ validate time zone"""
    timezone = request.args.get('timezone')
    if timezone:
        print(pytz.timezone(timezone))
        return g.time
    user_time = g.user.get('timezone')
    if user_time:
        print(pytz.timezone(user_time))
        return g.time
    Config.BABEL_DEFAULT_TIMEZONE
    return g.time


@app.route('/', strict_slashes=False)
def index() -> str:
    """simple route"""
    return render_template('index.html')


def get_user() -> dict:
    """returns a user dictionary"""
    id = request.args.get('login_as')
    if id and int(id) in users:
        return users.get(int(id))
    return None


@app.before_request
def before_request() -> None:
    """use get_user to find a user"""
    user = get_user()
    if user and user['locale'] in Config.LANGUAGES:
        g.user = user


if __name__ == '__main__':
    app.run()
