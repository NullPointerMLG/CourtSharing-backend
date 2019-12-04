import json
from flask_restful import Resource
from bson.json_util import dumps
from flask import request
from mongoengine import DoesNotExist, ValidationError
from bson import ObjectId
from models.event import Event as Event_model
from models.user import User as User_model
from models.sport import Sport as Sport_model
from utils.auth import Auth
from models.event import Event as Event_model
from models.user import User as User_model


# pylint: disable=E1101
class Event(Resource):

    def put(self, id):
        # pylint: disable=E1101
        args = request.get_json(force=True, silent=True)['params']
        headers = request.headers
        token_validation = Auth.auth_token(headers)
        if(token_validation != 'True'):
            return token_validation
        
        try:
            participant= User_model.objects.get(uuid=args['participantUUID'])
        except DoesNotExist:
            with open('utils/errorCodes.json', 'r') as errorCodes:
                return json.load(errorCodes)['USER_ERROR']['NOT_FOUND'], 500

        try:        
            event = Event_model.objects.get(id=id)
        except DoesNotExist:
            with open('utils/errorCodes.json', 'r') as errorCodes:
                return json.load(errorCodes)['EVENT_ERROR']['NOT_FOUND'], 500

        found = False
        for p in event['participants']:
            if p.id == participant.id:
                found = True
                event.update(pull__participants=participant.id)
                break   
        if not found:
            event.participants.append(ObjectId(participant.id))  
            try:       
                event.save()
            except ValidationError:
                with open('utils/errorCodes.json', 'r') as errorCodes:
                    return json.load(errorCodes)['EVENT_ERROR']['NOT_VALID'], 500
            return eval(dumps(event)), 200
            
        return 200
        