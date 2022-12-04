#!/usr/bin/python3
"""
    Flask test module
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def index():
    """ Return function for the corresponding route """
    return render_template(
        '8-cities_by_states.html',
        states=storage.all("State")
        .values()
    )


@app.teardown_appcontext
def destroy(exception):
    """ Destroy current session """
    storage.close()


if __name__ == '__main__':
    app.run("0.0.0.0", 5000, debug=True)
