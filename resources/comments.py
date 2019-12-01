import json
from flask_restful import Resource
from bson.json_util import dumps
from flask import request
from mongoengine import DoesNotExist
from bson import ObjectId
from models.event import Event as Event_model
from models.user import User as User_model
from models.sport import Sport as Sport_model
from models.comment import Comment as Comment_model
from utils.auth import Auth

# pylint: disable=E1101
class Comments(Resource):
    
    def post(self):
        # pylint: disable=E1101
        args = request.get_json(force=True, silent=True)['params']
        headers = request.headers
        token_validation = Auth.auth_token(headers)
        if(token_validation != 'True'):
            return token_validation

        user = User_model.objects.get(uuid=args['userUUID'])

        comment = Comment_model(user=user.id, event=args['eventID'], message=args['message'])
        comment.save()

        return eval(dumps(comment)), 200
