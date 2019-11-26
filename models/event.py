from mongoengine import Document
from mongoengine import StringField, IntField, ReferenceField
from datetime import datetime
from models.user import User
from models.sport import Sport


class Event(Document):
    creation_date = IntField(default=datetime.now(), required=True)
    event_date = IntField(required=True)
    title = StringField(max_length=150, required=True)
    description = StringField(max_length=1500)
    court_id = StringField(required=True)
    creator = ReferenceField(User)
    sport = ReferenceField(Sport)
