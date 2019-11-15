from flask_restful import Resource

class Event(Resource):
    def get(self):
        return "Events"