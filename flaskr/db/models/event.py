from mongoengine import Document
from mongoengine import DateTimeField, StringField, ReferenceField, ListField
from user import User

class Event(Document):
    creationDate = DateTimeField(required=True)
    eventDate = DateTimeField(required=True)
    title = StringField(max_length=50, required=True)
    description = StringField(max_length=300)
    courtId = StringField(max_length=300, required=True)
    assistants = ListField(ReferenceField(User))
    creator = ReferenceField(User, required=True)