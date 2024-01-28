#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage, State
from models.state import State
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id=None):
    for state in storage.all(State).values():
        if state.id == id:
            state = sorted(states, key=lambda state: state.name)

        return render_template("9-states.html", state=state)


@app.teardown_appcontext
def db_teardown(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)