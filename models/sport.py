from mongoengine import Document
from mongoengine import StringField, ImageField


class Sport(Document):
    name = StringField(max_length=60, required=True)
    resourceID = StringField(required=True)
    icon = ImageField(required=True)
