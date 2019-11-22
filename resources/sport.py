from flask_restful import Resource, reqparse
from bson.json_util import dumps
from flask import request
from bson import ObjectId
import datetime


class Sport(Resource):
    def __init__(self, mongo):
        self.mongo = mongo

    def get(self):

        query = []
        args = request.args

        sportID = args.get('sport-id')
        if sportID is not None:
            query.append({"$match": {"_id": ObjectId(sportID)}})

        data = self.mongo.db.sport.aggregate(query)

        return eval(dumps(data)), 200
