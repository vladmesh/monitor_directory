from typing import Dict

import flask
from flask import Flask
from config import DIRECTORY_PATH
import os

app = Flask(__name__)


def walkfn(dirname: str, json_data: Dict = None):
    if not json_data:
        json_data = dict()
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isdir(path):
            json_data[name] = dict()
            json_data[name] = walkfn(path, json_data=json_data[name])
        elif os.path.isfile(path):
            json_data.update({name: None})
    return json_data


@app.route('/')
def show_directory_content():
    json_data = walkfn(DIRECTORY_PATH)
    response = flask.jsonify(json_data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run()
