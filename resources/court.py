from flask_restful import Resource, reqparse
from bson.json_util import dumps, loads
from flask import request
import requests
import datetime
import json

class Court(Resource):

    def __init__(self, mongo):
        self.mongo = mongo

    
    def get(self):

        with open('resources/resource.json', "r") as jsonFile:# Open the JSON file for reading
            data = json.load(jsonFile) # Read the JSON into the buffer
            jsonFile.close() # Close the JSON file

            ## Working with buffered content
            resource_id = data["resource"] 

        response = requests.get('https://datosabiertos.malaga.eu/api/3/action/datastore_search?resource_id=' + resource_id) 
        data = response.json()
        data = data['result']['records']
        for record in data:
            record['INFOESP'] = loads(record['INFOESP'].replace("/", ""))
        return data, 200

