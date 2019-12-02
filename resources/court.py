from flask_restful import Resource, reqparse
from bson.json_util import dumps, loads
import json
from flask import request
from bson import ObjectId
import requests
from utils.auth import Auth
from utils.distance import Distance
from models.sport import Sport as Sport_model
# pylint: disable=E1101
class Court(Resource):

    
    def get(self):
        headers = request.headers
        token_validation = Auth.auth_token(headers)
        if(token_validation != 'True'):
            return token_validation

        query = []
        args = request.args

        sportID = args.get('sport-id')
        court_id = args.get('id')
        lat = args.get('lat')
        lon = args.get('lon')
        if sportID is not None:
            query.append({ "$match" : { "_id" : ObjectId(sportID) } })

        sports_data = Sport_model.objects.aggregate(*query) 
        
        sports_json = eval(dumps(sports_data))[0]
            
        resource_url = sports_json['resource_url']

        response = requests.get(resource_url) 
        data = response.json()
        data = data['features']
        if lat is not None and lon is not None:
            fdata = []
            for feature in data:
                record = feature['properties']
                record['INFOESP'] = record['INFOESP'][0]
                record.pop('PRECIOS', None)
                record.pop('HORARIOS', None)
                record.pop('DESCRIPCION', None)
                record.pop('CONTACTO', None)
                flat = float(feature['geometry']['coordinates'][0])
                flon = float(feature['geometry']['coordinates'][1])
                distance = Distance.calc_distance(lat, lon, flat, flon)
                if distance >= 0 and distance <= 5:
                    fdata.append(feature)
            return fdata, 200
        else:
            for feature in data:
                record = feature['properties']
                record['INFOESP'] = record['INFOESP'][0]
                record.pop('PRECIOS', None)
                record.pop('HORARIOS', None)
                record.pop('DESCRIPCION', None)
                record.pop('CONTACTO', None)
                if court_id is not None:
                    if int(court_id) == record['ID']:
                        return feature, 200  
    
        return data, 200
