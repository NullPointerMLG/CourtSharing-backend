from flask_restful import Resource, reqparse
from bson.json_util import dumps
import json

from flask import request
from bson import ObjectId
from flask import request
import datetime



class Transport(Resource):

    def __init__(self, mongo):
        self.mongo = mongo


    def get(self):

        query = []
        args = request.args

        transportID = args.get('transport-id')
        cond = args.get('cond')
        if cond=="true" and transportID is not None:
            query.append({ "$match" : { "_id" : ObjectId(transportID) } })

        data = self.mongo.db.transport.aggregate(query) 

        return eval(dumps(data)), 200
