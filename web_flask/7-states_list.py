#!/usr/bin/python3
"""
    Flask test module
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def index():
    """ Return function for the corresponding route """
    return render_template(
        '7-states_list.html',
        states=storage.all("State")
        .values()
    )


@app.teardown_appcontext
def destroy(exception):
    """ Destroy current session """
    storage.close()


if __name__ == '__main__':
    app.run("0.0.0.0", 5000, debug=True)
