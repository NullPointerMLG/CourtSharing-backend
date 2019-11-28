from mongoengine import Document
from mongoengine import StringField


class User(Document):
    uuid = StringField(min_lenght=1, max_length=128, required=True)
    name = StringField(max_length=100, required=True)
    photo_url = StringField(max_length=200, required=True)
