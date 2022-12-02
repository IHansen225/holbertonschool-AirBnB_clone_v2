#!/usr/bin/python3
"""
    Flask test module
"""
from flask import Flask, render_template

app = Flask(__name__, template_folder='./templates')


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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    """ Return function for the corresponding route """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """ Return function for the corresponding route """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n):
    """ Return function for the corresponding route """
    return render_template('5-number.html', number=str(n))


if __name__ == '__main__':
    app.run(debug=True)
