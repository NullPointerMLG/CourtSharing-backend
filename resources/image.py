import json
from flask_restful import Resource
from bson.json_util import dumps
from flask import request
from mongoengine import DoesNotExist, ValidationError
from bson import ObjectId
from models.event import Event as Event_model
from models.user import User as User_model
from utils.auth import Auth

# pylint: disable=E1101
class Image(Resource):
    
    def post(self):
        # pylint: disable=E1101
        args = request.get_json(force=True, silent=True)['params']
        headers = request.headers
        token_validation = Auth.auth_token(headers)
        if(token_validation != 'True'):
            return token_validation

        try:
            event = Event_model.objects.get(id=ObjectId(args['eventID']))
        except DoesNotExist:
            with open('utils/errorCodes.json', 'r') as errorCodes:
                return json.load(errorCodes)['EVENT_ERROR']['NOT_FOUND'], 500

        photo_url = args['photoURL']
        found = False
        for url in event['photos']:
            if url == photo_url:
                found = True
                event.update(pull__photos=photo_url)
                break   
        if not found:
            event.photos.append(photo_url)  
            try:       
                event.save()
            except ValidationError:
                with open('utils/errorCodes.json', 'r') as errorCodes:
                    return json.load(errorCodes)['EVENT_ERROR']['NOT_VALID'], 500
            return eval(dumps(event)), 200

        return photo_url, 200
