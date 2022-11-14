from flask import flask

app = flask(__name__)


@app.route("/")
def hello():
    return "Hello,world"


@app.route('/')
def hello():
    return 'hi, i ivan'
