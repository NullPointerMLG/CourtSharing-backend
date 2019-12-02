from flask_restful import Resource, reqparse
from bson.json_util import dumps
import json

from flask import request
from bson import ObjectId
import requests
import datetime
from mongoengine import DoesNotExist
from models.transport import Transport as Transport_model
from utils.distance import Distance
from utils.auth import Auth



class Parking(Resource):

    def get(self):
    # pylint: disable=E1101
        headers = request.headers
        token_validation = Auth.auth_token(headers)
        if(token_validation != 'True'):
            return token_validation

        query = []
        args = request.args

        transport_id = args.get('id')
        lat = args.get('lat')
        lon = args.get('lon')
        if transport_id is not None:
            query.append({ "$match" : { "_id" : ObjectId(transport_id) } })

        transports_data = Transport_model.objects.aggregate(*query) 
        
        transports_json = eval(dumps(transports_data))[0]

        resource_url = transports_json['resource_url']

        response = requests.get(resource_url) 
        data = response.json()
        data = data['features']
        if lat is not None and lon is not None:
            fdata = []
            for feature in data:
                record = feature['properties']
                record.pop('timestamp', None)
                record.pop('begin', None)
                record.pop('end', None)
                record.pop('altitudemode', None)
                record.pop('tessellate', None)
                record.pop('extrude', None)
                record.pop('visibility', None)
                record.pop('draworder', None)
                record.pop('icon', None)
                flat = float(feature['geometry']['coordinates'][0])
                flon = float(feature['geometry']['coordinates'][1])
                distance = Distance.calc_distance(lat, lon, flat, flon)
                if distance >= 0 and distance <= 5:
                    print(distance)
                    fdata.append(feature)
            return fdata, 200
        else:
            for feature in data:
                record = feature['properties']
                record.pop('timestamp', None)
                record.pop('begin', None)
                record.pop('end', None)
                record.pop('altitudemode', None)
                record.pop('tessellate', None)
                record.pop('extrude', None)
                record.pop('visibility', None)
                record.pop('draworder', None)
                record.pop('icon', None)
        return data, 200  