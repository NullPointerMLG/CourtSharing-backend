from mongoengine import Document
from mongoengine import StringField


class Transport(Document):
    name = StringField(max_length=60, required=True)
    resource_id = StringField(required=True)