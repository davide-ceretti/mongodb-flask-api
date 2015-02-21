# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask("api")
mongo = PyMongo(app)


@app.route("/api/hello")
def hello():
    return "Hello, world!"
