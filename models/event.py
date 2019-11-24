from mongoengine import Document
from mongoengine import DateTimeField, StringField
from datetime import datetime
import time


class Event(Document):
    creation_date = DateTimeField(default=datetime.now(), required=True)
    event_date = DateTimeField(required=True)
    title = StringField(max_length=150, required=True)
    description = StringField(max_length=1500)
    courtID = StringField(required=True)
    creatorUID = StringField(required=True)
