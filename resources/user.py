from flask_restful import Resource, reqparse
from bson.json_util import dumps
from flask import request

class User(Resource):
    def __init__(self, mongo):
        self.mongo = mongo

    def get(self):
        data = self.mongo.db.user.find()
        return dumps(data), 200

    def post(self):
        uuid = "example"
        user = self.mongo.db.user.find({'UUID':uuid})
        if user.count() == 0:
            uuid = "new_example"
            self.mongo.db.user.insert({'UUID':uuid})
            user = self.mongo.db.user.find({'UUID':uuid})
        return dumps(user), 200
        
