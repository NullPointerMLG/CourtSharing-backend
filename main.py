import os

from flask import Flask
from config import MONGO_URL

from flask_restful import Api

from controllers.event import Event
from controllers.court import Court
from controllers.sport import Sport


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
API.add_resource(Event, '/events', resource_class_kwargs={'mongo':mongo})
API.add_resource(Court, '/courts', resource_class_kwargs={'mongo':mongo})
API.add_resource(Sport, '/sports', resource_class_kwargs={'mongo':mongo})

if __name__ == '__main__':
    print("Deploying service in port 5000")
    APP.run(host="0.0.0.0", port=5000, debug=True)