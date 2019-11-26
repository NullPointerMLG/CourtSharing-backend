from flask_restful import Resource, reqparse
from bson.json_util import dumps
from flask import request
import requests
import datetime


class Court(Resource):

    def get(self):
        response = requests.get(
            'https://datosabiertos.malaga.eu/api/3/action/datastore_search?resource_id=f6375d3b-e9cb-4549-a20f-6f276ab25d8a')
        return response.json(), 200
