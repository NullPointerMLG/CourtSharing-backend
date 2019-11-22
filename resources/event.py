from flask_restful import Resource, reqparse
from bson.json_util import dumps
from flask import request
import datetime

class Event(Resource):
    def __init__(self, mongo):
        self.mongo = mongo

    def get(self):
        query = []
        args = request.args

        event_date = args.get('date')
        if event_date is not None:
            query.append({ "$match" : { "eventDate" : int(event_date) } })
        
        court_id = args.get('court')
        if court_id is not None:
            query.append({ "$match" : { "courtID" : int(court_id) } })
    
        courts = self.mongo.db.event.aggregate(query)
        data = []
        for court in courts:
            user = self.mongo.db.user.find_one(court['creator'])
            court['creator'] = user
            data = court

        return eval(dumps(data)), 200

    def post(self):
        # TODO: validate parameters
        event = request.get_json(force=True)
        creation_date = datetime.datetime.now()
        event_date = event['eventDate']
        title = event['title']
        description = event['description']
        court_id = event['courtID']
        creator = event['creator']

        # TODO: Add error handler

        event = self.mongo.db.event.insert({
            "creationDate": creation_date   ,
            "eventDate": event_date,
            "title": title,
            "description": description,
            "courtID": court_id,
            "creator": creator
        })

        return eval(dumps(event)), 200
