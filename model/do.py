import datetime
from mongoengine import Document, DateTimeField, FileField, ListField, ReferenceField, StringField, CASCADE, PULL
from model.config import Config


class Member(Document):
    id_no = StringField(max_length=7, regex='\d{2}-\d{4}', required=True)
    name = StringField(max_length=50, required=True)
    major = StringField(max_length=4, required=True)
    image = FileField(default=None)
    laptops = ListField(ReferenceField('Laptop'), default=None)


class Laptop(Document):
    serial_no = StringField(max_length=50, required=True)
    make = StringField(max_length=10, required=True)
    owner = ReferenceField('Member')


class Log(Document):
    member = ReferenceField('Member')
    time_in = DateTimeField(default=datetime.datetime.now().replace(microsecond=0))
    time_out = DateTimeField(None)

    meta = {'collection': Config.get_collection()}


Laptop.register_delete_rule(Member, 'laptops', PULL)
Member.register_delete_rule(Laptop, 'owner', CASCADE)
