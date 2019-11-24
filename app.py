import os

from flask import Flask
from config import MONGO_URL

from flask_restful import Api

from resources.event import Event
from resources.court import Court
from resources.sport import Sport
from resources.login import Login


import json
import datetime
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
import firebase_admin
from flask_cors import CORS
import mongoengine

if __name__ == '__main__':
    db = mongoengine.connect(alias="default", host=MONGO_URL)

APP = Flask(__name__)
CORS(APP)
API = Api(APP)

APP.config["MONGO_URI"] = MONGO_URL
APP.config['MONGODB_SETTINGS'] = {'db':'testing', 'alias':'default'}

mongo = PyMongo(APP)

# Endpoints
API.add_resource(Event, '/events', resource_class_kwargs={'mongo': mongo})
API.add_resource(Login, '/login', resource_class_kwargs={'mongo': mongo})
API.add_resource(Court, '/courts', resource_class_kwargs={'mongo': mongo})
API.add_resource(Sport, '/sports', resource_class_kwargs={'mongo': mongo})

if __name__ == '__main__':
    print("Deploying service in port 5000")
    APP.run(host="0.0.0.0", port=5000, debug=True)
