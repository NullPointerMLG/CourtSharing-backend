from flask_restful import Resource
from bson.json_util import dumps
from bson import ObjectId
from flask import request
from mongoengine import DoesNotExist
from models.sport import Sport as Sport_model


class Sport(Resource):

    def get(self):
    # pylint: disable=E1101      
        args = request.args
        sport_id = args.get('sport_id')

        try:
            query = []
            if sport_id is not None:
                query.append({"$match": {"id": ObjectId(sport_id)}})
        except DoesNotExist:
            return False
        sport = eval(dumps(Sport_model.objects.aggregate (*query)))

        return sport, 200
