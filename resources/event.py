import json
from flask_restful import Resource
from bson.json_util import dumps
from flask import request
from mongoengine import DoesNotExist
from bson import ObjectId
from models.event import Event as Event_model
from models.user import User as User_model
from models.sport import Sport as Sport_model
from utils.auth import Auth

# pylint: disable=E1101
class Event(Resource):

    def get(self):
        args = request.get_json(force=True, silent=True)
        headers = request.headers
        token_validation = Auth.auth_token(headers)
        if(token_validation != 'True'):
            return token_validation

        event_date = court_id = event_sport = None
        if args is not None:
            event_date = args.get('date')
            court_id = args.get('court') 
            event_sport = args.get('sport')

        try:          
            query = []
            if event_sport is not None:
                query.append({"$match": {"sport": ObjectId(event_sport)}})
            if event_date is not None:
                query.append({"$match": {"event_date":int(event_date)}})
            if court_id is not None:
                query.append({"$match": {"court_id":int(court_id)}})

            events = eval(dumps(Event_model.objects.aggregate (*query)))   
            for event in events:
                query = User_model.objects.get(id=event['creator']['$oid']) 
                data = query.to_json()
                creator = json.loads(data)
                event['creator'] = creator
            return events, 200
        except DoesNotExist:
             with open('utils/errorCodes.json', 'r') as errorCodes:
                return json.load(errorCodes)['EVENT_ERROR']['NOT_FOUND'], 500
    
    def post(self):
        # TODO: validate parameters
        args = request.get_json(force=True, silent=True)
        token_validation = Auth.auth_token(args)
        if(token_validation != 'True'):
            return token_validation

        if args is None:
            return False, 500
        event_data = args

        new_event = Event_model(
            event_date=event_data['event_date'],
            title=event_data['title'],
            description=event_data['description'],
            court_id=event_data['court_id'],
            creator=User_model.objects(id=event_data['creator_id']),
            sport=Sport_model.objects(id=event_data['sport_id'])
        )
        new_event.save()
        event = new_event.to_json()
        return eval(dumps(event)), 200