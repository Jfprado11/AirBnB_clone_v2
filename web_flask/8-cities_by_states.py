#!/usr/bin/python3
"""server for displaying cities and states"""

from flask import Flask
from flask.templating import render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """display a html with the states and cities"""
    states = storage.all(State)
    cities = storage.all(City)
    return render_template("8-cities_by_states.html", states=states,
                           cities=cities)


@app.teardown_appcontext
def closing(exception):
    """to close the conection"""
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
