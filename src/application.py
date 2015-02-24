# -*- coding: utf-8 -*-
import json

from flask import Flask, make_response, request
from flask.ext.pymongo import PyMongo

app = Flask("api")
mongo = PyMongo(app)


@app.route("/api/hello", methods=['GET'])
def hello():
    return make_response("Hello, world!", 200)


@app.route("/api/user", methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        user_dict = json.loads(request.data.decode('utf-8'))
        mongo.db.user.insert(user_dict)
        _patch_dict(user_dict)
        response = make_response(json.dumps(user_dict), 201)
        response.headers = {'Content-Type': 'application/json'}
        return response


def _patch_dict(my_dict):
    _id = my_dict.pop('_id', None)
    if _id is None:
        raise ValueError("Can't patch dict without _id key")
    my_dict['id'] = str(_id)
