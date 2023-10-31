#!/usr/bin/env python3
"""1-app.py - Basic Babel setup """


from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Locale configuration"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """determine the best match supported languages."""
    return request.accept_lanquages.best_match(app.config["LANGUAGES"])


@app.route('/', strict_slashes=False)
def index() -> str:
    """simple route"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
