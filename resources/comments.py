import json
from flask_restful import Resource
from bson.json_util import dumps
from flask import request
from mongoengine import DoesNotExist, ValidationError
from models.user import User as User_model
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

        try:
            user = User_model.objects.get(uuid=args['userUUID'])
        except DoesNotExist:
            with open('utils/errorCodes.json', 'r') as errorCodes:
                return json.load(errorCodes)['USER_ERROR']['NOT_FOUND'], 500

        try:
            comment = Comment_model(user=user.id, event=args['eventID'], message=args['message'])
            comment.save()
        except ValidationError:
             with open('utils/errorCodes.json', 'r') as errorCodes:
                return json.load(errorCodes)['COMMENT_ERROR']['NOT_VALID'], 500

        return eval(dumps(comment)), 200
