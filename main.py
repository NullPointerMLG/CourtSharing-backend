'''
Main package the deploy a service to request Tensorflow models.
'''

import os

from flask import Flask
from config import MONGO_URL
from flask import jsonify

from flask_restful import Api

from controllers.event import Event

import json
import datetime
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask_pymongo import PyMongo

APP = Flask(__name__)
API = Api(APP)

APP.config["MONGO_URI"] = MONGO_URL
mongo = PyMongo(APP)

# Endpoints
API.add_resource(Event, '/event')


if __name__ == '__main__':
    print("Deploying service in port 5000")
    APP.run(host="0.0.0.0", port=5000, debug=True)