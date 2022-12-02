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

if __name__ == '__main__':
    app.run(debug = True)
