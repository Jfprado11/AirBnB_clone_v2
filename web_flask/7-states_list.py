#!/usr/bin/python3
"""using flask to create a dinamic Airbnb_clone"""
from flask import Flask
from flask.templating import render_template
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """showing all the states of the database"""
    from models.state import State
    states = storage.all(State)
    render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def closing():
    """to close the conection"""
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
