from flask_restful import Resource, reqparse
from bson.json_util import dumps
from flask import request
import firebase_admin
from firebase_admin import auth

class Login(Resource):
    def __init__(self, mongo):
        self.mongo = mongo
        firebase_admin.initialize_app()        

    def post(self): 
        event = request.get_json(force=True)
        print(event);
        return dumps(event), 200
        token = 'a'
        decoded_token = auth.verify_id_token(token)
        uuid = decoded_token['uid']
        user = self.mongo.db.user.find({'UUID':uuid})
        if user.count() == 0:
            uuid = "new_example"
            self.mongo.db.user.insert({'UUID':uuid})
            user = self.mongo.db.user.find({'UUID':uuid})
        return dumps(user), 200

