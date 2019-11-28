import json
from flask_restful import Resource
from flask import request
import requests
from utils.auth import Auth

class Court(Resource):

    def get(self):
        args = request.get_json(force=True, silent=True)
        token_validation = Auth.auth_token(args)
        if(token_validation != 'True'):
            return token_validation

        response = requests.get(
            'https://datosabiertos.malaga.eu/api/3/action/datastore_search?resource_id=f6375d3b-e9cb-4549-a20f-6f276ab25d8a')
        return response.json(), 200
