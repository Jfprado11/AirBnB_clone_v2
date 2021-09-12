#!/usr/bin/python3
"""flask aplication for Airbnb clone"""

from flask import Flask
from flask.templating import render_template
from models import state
from models.state import State
from models.city import City
from models import storage


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """show the states"""
    states = storage.all(State)
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """show the specific state with its cities"""
    states = storage.all(State)
    if any(id == value[6:] for value in states.keys()):
        key = "State." + id
        state = states[key]
        return render_template("9-states.html", state=state)
    else:
        return render_template("9-states.html")


@app.teardown_appcontext
def closing(exception):
    """to close the conection"""
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
