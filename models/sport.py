from mongoengine import Document
from mongoengine import StringField


class Sport(Document):
    name = StringField(max_length=60, required=True)
    resource_id = StringField(required=True)
    icon_url = StringField(required=True)
    resource_url = StringField(required=True)
