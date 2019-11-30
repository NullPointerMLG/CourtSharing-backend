from mongoengine import Document
from mongoengine import StringField, ReferenceField
from models.user import User
from models.event import Event

class Comment(Document):
    user = ReferenceField(User, required=True)
    message = StringField(max_length=1500, required=True)
    event = ReferenceField(Event, reverse_delete_rule=mongoengine.CASCADE)