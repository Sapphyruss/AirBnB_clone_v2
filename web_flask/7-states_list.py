#!/usr/bin/python3
"""Fetch data from the storage engine"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def end_session(exception):

    storage.close()


@app.route("/states_list", strict_slashes=False)
def List_of_states():

    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
