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


@app.route("/")
def hello_world():
    """ Displays Hello message """
    return "Hello HBNB!"


@app.route("/hbnb")
def display_hbnb():
    """ Displays HBNB """
    return "HBNB"


@app.route("/c/<text>")
def display_c_text(text):
    """ Displays message with dynamic texr """
    return f"C {escape(text.replace('_', ' '))}"


@app.route("/python/<text>")
@app.route("/python/")
def display_python_text(text="is cool"):
    """ Displays message with dynamic text"""
    return f"Python {escape(text.replace('_', ' '))}"


@app.route("/number/<int:n>")
def display_if_number(n):
    """ Displays only number"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def display_template_number(n):
    """ Displays only number using a template"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def display_number_odd_or_even(n):
    """ Displays only number using a template"""
    return render_template("6-number_odd_or_even.html", n=n)


@app.route("/states_list")
def states_list():
    """ Displays a list of state id and name"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
