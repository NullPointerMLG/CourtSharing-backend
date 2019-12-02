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

        result = []
        args = request.args

        lat = args.get('lat')
        lon = args.get('lon')

        transports_data = Transport_model.objects

        for transport in transports_data:
            resource_url = transport['resource_url']

            response = requests.get(resource_url)
            data = response.json()
            data = data['features']
            if lat is not None and lon is not None:
                currentData = []
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
                    record['marker_url'] = transport.marker_url
                    flat = float(feature['geometry']['coordinates'][0])
                    flon = float(feature['geometry']['coordinates'][1])
                    distance = Distance.calc_distance(lat, lon, flat, flon)
                    if distance >= 0 and distance <= 1:
                        currentData.append(feature)
                result.append(
                    {"type": transport.name, "data": currentData, "marker_url": transport.marker_url})
        
        return result, 200
