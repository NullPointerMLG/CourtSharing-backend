from flask_restful import Resource
from bson.json_util import dumps
from bson import ObjectId
from flask import request
from mongoengine import DoesNotExist
from models.sport import Sport as Sport_model
from utils.auth import Auth




class Sport(Resource):


    def get(self):
    # pylint: disable=E1101
        args = request.args
        headers = request.headers
        token_validation = Auth.auth_token(headers)
        if(token_validation != 'True'):
            return token_validation

        sport_id = None
        if args is not None:
            sport_id = args.get('id')

        try:
            query = []
            if sport_id is not None:
                query.append({"$match": {"_id": ObjectId(sport_id)}})
        except DoesNotExist:
            return False
        sport = eval(dumps(Sport_model.objects.aggregate (*query)))

        return sport, 200
