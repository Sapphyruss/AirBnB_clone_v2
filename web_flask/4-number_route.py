#!/usr/bin/python3
"""Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_is_fun(text):
    txt = text.replace("_", " ")
    return f"C {txt}"


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def Python_is_cool(text="is_cool"):
    txt = text.replace("_", " ")
    return f"Python {txt}"


@app.route("/number/<int:n>")
def Is_it_a_number(n):
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
