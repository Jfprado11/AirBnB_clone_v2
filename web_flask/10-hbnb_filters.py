#!/usr/bin/python3
"""displaying the page of the airbnb clone"""

from flask import Flask
from flask.templating import render_template
from models import storage
from models import state
from models.amenity import Amenity
from models.city import City
from models.state import State

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """show the diferents places and amenities"""
    states = storage.all(State)
    cities = storage.all(City)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html", states=states, cities=cities, amenities=amenities)


@app.teardown_appcontext
def closing(exception):
    """to close the conection"""
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
