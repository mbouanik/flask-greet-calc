# Put your app in here.
from flask import Flask, request
from operations import *

app = Flask(__name__)


@app.route("/")
def home():
    return "hello"


@app.route("/add")
def addition():
    a = request.args["a"]
    b = request.args["b"]
    return f"{add(int(a), int(b))}"


@app.route("/sub")
def substract():
    a = request.args["a"]
    b = request.args["b"]
    return f"{sub(int(a), int(b))}"


@app.route("/mult")
def multiply():
    a = request.args["a"]
    b = request.args["b"]
    return f"{mult(int(a), int(b))}"


@app.route("/div")
def divide():
    a = request.args["a"]
    b = request.args["b"]
    return f"{div(int(a), int(b))}"


if __name__ == "__main__":
    app.run(debug=True)
