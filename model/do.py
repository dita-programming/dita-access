import datetime

from mongoengine import Document
from mongoengine import DateTimeField, FileField, ListField, ReferenceField, SequenceField, StringField
from mongoengine import CASCADE, PULL

from model.config import Config


class Member(Document):
    id_no = StringField(max_length=7, regex='\d{2}-\d{4}', required=True, primary_key=True)
    name = StringField(max_length=50, required=True)
    major = StringField(max_length=4, required=True)
    image = FileField(default=None)
    laptops = ListField(ReferenceField('Laptop'), default=None)

    def __repr__(self):
        return "%s - %s" % (self.id_no, self.name)


class Laptop(Document):
    serial_no = StringField(max_length=50, required=True, primary_key=True)
    make = StringField(max_length=10, required=True)
    owner = ReferenceField('Member')

    def __repr__(self):
        return "%s - %s" % (self.serial_no, self.make)


class LogItem(Document):
    index = SequenceField(primary_key=True)
    member = ReferenceField('Member')
    time_in = DateTimeField(default=datetime.datetime.now().replace(microsecond=0))
    time_out = DateTimeField(None)

    meta = {'collection': Config.get_collection()}


Laptop.register_delete_rule(Member, 'laptops', PULL)
Member.register_delete_rule(Laptop, 'owner', CASCADE)
