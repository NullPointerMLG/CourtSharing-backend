from flask_restful import Resource, reqparse
from bson.json_util import dumps
import json

from flask import request
from bson import ObjectId
from flask import request
import datetime
from mongoengine import DoesNotExist
from models.transport import Transport as Transport_model
from utils.auth import Auth



class Transport(Resource):

    def get(self):
    # pylint: disable=E1101
        args = request.args
        headers = request.headers
        token_validation = Auth.auth_token(headers)
        if(token_validation != 'True'):
            return token_validation

        transport_id = None
        cond = None
        if args is not None:
            transport_id = args.get('id')
         #   cond = args.get('cond')

        try:
            query = []
            if transport_id is not None:
                query.append({"$match": {"_id": ObjectId(transport_id)}})
           # if cond=="true" and transportID is not None:
               # query.append({ "$match" : { "id" : ObjectId(transport_id) } })
        except DoesNotExist:
            return False

        transport = eval(dumps(Transport_model.objects.aggregate (*query)))

        return transport, 200    
