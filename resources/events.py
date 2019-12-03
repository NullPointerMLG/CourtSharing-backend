import json
from flask_restful import Resource
from bson.json_util import dumps
from flask import request
from mongoengine import DoesNotExist, ValidationError
from bson import ObjectId
from models.event import Event as Event_model
from models.user import User as User_model
from models.sport import Sport as Sport_model
from models.comment import Comment as Comment_model
from utils.auth import Auth

# pylint: disable=E1101
class Events(Resource):

    def get(self):
        args = request.args
        headers = request.headers
        token_validation = Auth.auth_token(headers)
        if(token_validation != 'True'):
            return token_validation

        event_date = court_id = event_sport = None
        if args is not None:
            event_date = args.get('date')
            court_id = args.get('court') 
            event_sport = args.get('sport')
        
        query = []
        events = []
        if event_sport is not None:
            query.append({"$match": {"sport": ObjectId(event_sport)}})
        if event_date is not None:
            query.append({"$match":  {"event_date": {"$gte" :int(event_date)}}})
        if court_id is not None:
            query.append({"$match": {"court_id":int(court_id)}})
        result = Event_model.objects.aggregate (*query) 

        for res in result:
            event = {}
            event['id'] = eval(dumps(res['_id']))['$oid']
            event['eventDate'] = res['event_date']
            event['creationDate'] = res['creation_date']
            event['title'] = res['title']
            event['description'] = res['description']
            event['sport'] = res['sport']
            event['courtID'] = res['court_id']

            try:
                creator =  User_model.objects.get(id=res['creator'])
            except DoesNotExist:
                with open('utils/errorCodes.json', 'r') as errorCodes:
                    return json.load(errorCodes)['USER_ERROR']['NOT_FOUND'], 500
                
            creator_serialized = {}
            creator_serialized['uuid'] = creator.uuid
            creator_serialized['name'] = creator.name
            creator_serialized['photoURL'] = creator.photo_url
            event['creator'] = creator_serialized   

            participants_from_db = res['participants']
            participants = []
            for p in participants_from_db:
                user =  User_model.objects.get(id=p)
                user_serialized = {}
                user_serialized['uuid'] = user.uuid
                user_serialized['name'] = user.name
                user_serialized['photoURL'] = user.photo_url
                participants.append(user_serialized)
            event['participants'] = participants
                        
            comments_from_db = Comment_model.objects(event=event['id'])
            comments = []
            for c in comments_from_db:
                comment = {}
                user_serialized = {}
                user_serialized['uuid'] = c.user.uuid
                user_serialized['name'] = c.user.name
                user_serialized['photoURL'] = c.user.photo_url
                comment['user'] = user_serialized
                comment['message'] = c.message
                comment['id'] = eval(dumps(c.id))['$oid']
                comments.append(comment)
            event['comments'] = comments

            events.append(eval(dumps(event)))
        return events, 200


    
    def post(self):
        # TODO: validate parameters
        args = request.get_json(force=True, silent=True)
        token_validation = Auth.auth_token(request.headers)
        if(token_validation != 'True'):
            return token_validation

        if args is None:
            return False, 500
        event_data = args
        
        try:
            user = User_model.objects.get(uuid=args['creator_uuid'])
        except DoesNotExist:
            with open('utils/errorCodes.json', 'r') as errorCodes:
                    return json.load(errorCodes)['USER_ERROR']['NOT_FOUND'], 500
        
        new_event = Event_model(
            event_date=int(event_data['event_date']),
            title=event_data['title'],
            description=event_data['description'],
            court_id=event_data['court_id'],
            creator=user['id'],
            sport=event_data['sport_id']['$oid'],
            participants=[user['id']],
            photo=event_data['photo']
        )

        try:
            new_event.save()
        except ValidationError:
            with open('utils/errorCodes.json', 'r') as errorCodes:
                    return json.load(errorCodes)['EVENT_ERROR']['NOT_VALID'], 500

        event = new_event.to_json()
        return eval(dumps(event)), 200