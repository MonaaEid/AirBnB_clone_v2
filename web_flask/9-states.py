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
    return render_template('8-cities_by_states.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    if state is None:
        state = None
    else:
        state = storage.get(State, id)

        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('9-states_id.html', state=state, cities=cities)


@app.teardown_appcontext
def db_teardown(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
