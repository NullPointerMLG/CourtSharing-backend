from flask_restful import Resource, reqparse
from bson.json_util import dumps, loads
from flask import request
import requests
import datetime

class Court(Resource):
    def __init__(self, mongo):
        self.mongo = mongo

    def get(self):
        response = requests.get('https://datosabiertos.malaga.eu/api/3/action/datastore_search?resource_id=f6375d3b-e9cb-4549-a20f-6f276ab25d8a') 
        data = response.json()
        data = data['result']['records']
        for record in data:
            record['INFOESP'] = loads(record['INFOESP'].replace("/", ""))
        return data, 200

