#!/usr/bin/python3
"""this will create the flask app to
do the web aplication for Airbnb clone"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """returs a string to see if it works"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbhb():
    """returns a string displaying HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    value = text.replace("_", " ")
    return "C {}".format(escape(value))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
