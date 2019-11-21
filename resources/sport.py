from flask_restful import Resource, reqparse
from bson.json_util import dumps
from flask import request
import datetime

class Sport(Resource):
    def __init__(self, mongo):
        self.mongo = mongo

    def get(self):

        data = self.mongo.db.sport.find()
        
        return dumps(data), 200

