from flask_restful import Resource, reqparse
from bson.json_util import dumps, loads
import json
from flask import request
from bson import ObjectId
import requests
from utils.auth import Auth
from models.sport import Sport as Sport_model
# pylint: disable=E1101
class Court(Resource):

    
    def get(self, id):
        headers = request.headers
        token_validation = Auth.auth_token(headers)
        if(token_validation != 'True'):
            return token_validation

        query = []
        args = request.args

        sportID = args.get('sport-id')
        if sportID is not None:
            query.append({ "$match" : { "_id" : ObjectId(sportID) } })

        sports_data = Sport_model.objects.aggregate(*query) 
        
        sports_json = eval(dumps(sports_data))[0]
            
        resource_url = sports_json['resource_url']

        response = requests.get(resource_url) 
        data = response.json()
        data = data['features']
        for feature in data:
            record = feature['properties']
            record['INFOESP'] = record['INFOESP'][0]
            record.pop('PRECIOS', None)
            record.pop('HORARIOS', None)
            record.pop('DESCRIPCION', None)
            record.pop('CONTACTO', None)
            if id is not None:
                if int(id) == record['ID']:
                    return [feature], 200  
    
        return data, 200
