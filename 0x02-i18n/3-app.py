#!/usr/bin/env python3
"""3-app.py - Parametrize templates """


from flask import Flask, render_template, request
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """determine the best match supported languages."""
    return request.accept_languages.best_match(["en", "fr"])


@app.route('/', strict_slashes=False)
def index() -> str:
    """simple route"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
