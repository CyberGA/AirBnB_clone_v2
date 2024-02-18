#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: display "HBNB"
    /c/<text>: display “C ” followed by the value
                of the text variable (replace
                underscore _ symbols with a space)
    /python/<text>: display “Python ”, followed by the
                    value of the text variable (replace
                    underscore _ symbols with a space)
    /number/<n>: display “n is a number” only if n is an integer
    /number_template/<n>: display a HTML page only if n is an
                          integer: H1 tag: “Number: n”
                          inside the tag BODY
    /number_odd_or_even/<n>: display a HTML page only if n is an
                             integer: H1 tag: “Number: n is
                             even|odd” inside the tag BODY
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from markupsafe import escape

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def states_list():
    """ Displays a list of state id and name"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(context):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
