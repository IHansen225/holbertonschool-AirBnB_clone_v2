#!/usr/bin/python3
"""
    Flask test module
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', defaults={'id': None}, strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """ Render a particular state """
    states = storage.all("State")
    if id is None:
        return render_template(
            '9-states.html',
            states=states.values(),
            len=len(states)
        )
    key = "State.{}".format(id)
    states = states[key] if key in states.keys() else None
    return render_template('9-states.html', states=states, len=1)


@app.teardown_appcontext
def destroy(exception):
    """ Destroy current session """
    storage.close()


if __name__ == '__main__':
    app.run("0.0.0.0", 5000, debug=True)
