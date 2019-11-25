from flask_restful import Resource, reqparse
from bson.json_util import dumps
from flask import request
import datetime
from models.event import Event as Event_model


class Event(Resource):
    def __init__(self, mongo):
        self.mongo = mongo

    def get(self):
        query = []
        args = request.args

        event_date = args.get('date')
        if event_date is not None:
            query.append({"$match": {"eventDate": int(event_date)}})

        court_id = args.get('court')
        if court_id is not None:
            query.append({"$match": {"courtID": int(court_id)}})

        event_sport = args.get('sport')
        if event_sport is not None:
            query.append({"$match": {"sport": event_sport}})

        courts = self.mongo.db.event.aggregate(query)
        data = []
        for court in courts:
            user = self.mongo.db.user.find_one(court['creator'])
            court['creator'] = user
            data.append(court)

        return eval(dumps(data)), 200

    def post(self):
        # TODO: validate parameters
        event_data = request.get_json(force=True, silent=True)

        new_event = Event_model(
            creation_date=datetime.datetime.now(),
            event_date=event_data['eventDate'],
            title=event_data['title'],
            description=event_data['description'],
            courtID=event_data['courtID'],
            creatorUID=event_data['creator']
        )
        new_event.save()

        return eval(dumps(new_event)), 200
