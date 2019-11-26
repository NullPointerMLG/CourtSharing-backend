from flask_restful import Resource, reqparse
from bson.json_util import dumps
from flask import request
from bson import ObjectId
import datetime
from models.sport import Sport as Sport_model
from mongoengine import DoesNotExist


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
