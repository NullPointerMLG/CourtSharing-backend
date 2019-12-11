import time
from mongoengine import Document
from mongoengine import StringField, IntField, ReferenceField, ListField, CASCADE
from models.user import User
from models.sport import Sport

class Event(Document):
    creation_date = IntField(default=time.time(), required=True)
    event_date = IntField(required=True)
    title = StringField(max_length=150, required=True)
    description = StringField(max_length=1500)
    court_id = IntField(required = True)
    creator = ReferenceField(User, required=True)
    sport = ReferenceField(Sport, required=True, reverse_delete_rule=CASCADE)
    photos = ListField(StringField(required=False))
    participants = ListField(ReferenceField(User), required = True)
