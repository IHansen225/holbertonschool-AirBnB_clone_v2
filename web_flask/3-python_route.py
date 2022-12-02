#!/usr/bin/python3
"""
    Flask test module
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ Return function for the corresponding route """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Return function for the corresponding route """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text_route(text):
    """ Return function for the corresponding route """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """ Return function for the corresponding route """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)

if __name__ == '__main__':
    app.run(debug=True)
