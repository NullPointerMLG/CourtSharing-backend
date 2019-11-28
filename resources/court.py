from flask_restful import Resource, reqparse
from bson.json_util import dumps, loads
import json
from flask import request
from bson import ObjectId
import requests
from utils.auth import Auth

class Court(Resource):

    
    def get(self):
        headers = request.headers
        token_validation = Auth.auth_token(headers)
        if(token_validation != 'True'):
            return token_validation

        query = []
        args = request.args

        sportID = args.get('id')
        if sportID is not None:
            query.append({ "$match" : { "_id" : ObjectId(sportID) } })

        data = self.mongo.db.sport.aggregate(query) 
        
        jsonAux = eval(dumps(data))

        #Esta es una de las formas de hallar el resource_id nos podemos quedar con el 0 pq solo lo vamos a usar cuando busquemos un deporte especific
        # por lo que solo deberia tener un elemento.
        resource_id = jsonAux[0]['resource_id']

        response = requests.get('https://datosabiertos.malaga.eu/api/3/action/datastore_search?resource_id=' + resource_id) 
        data = response.json()
        data = data['result']['records']
        for record in data:
            record['INFOESP'] = loads(record['INFOESP'].replace("/", ""))
            record.pop('PRECIOS', None)
            record.pop('HORARIOS', None)
            record.pop('DESCRIPCION', None)
            record.pop('CONTACTO', None)
        return data, 200
