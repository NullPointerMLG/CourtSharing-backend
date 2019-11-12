from mongoengine import Document
from mongoengine import DateTimeField, StringField, ReferenceField, ListField

class User(Document):
    UUID = StringField(max_length=60, required=True)
