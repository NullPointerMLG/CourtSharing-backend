from flask_restful import Resource, reqparse
from bson.json_util import dumps
from flask import request
import datetime

class Event(Resource):
    def __init__(self, mongo):
        self.mongo = mongo

    def get(self):
        data = self.mongo.db.event.find()
        return dumps(data), 200

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
            "courtId": court_id,
            "creator": creator
        })

        return dumps(event), 200
