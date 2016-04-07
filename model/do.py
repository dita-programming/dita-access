import datetime

from mongoengine import Document
from mongoengine import DateTimeField, FileField, ListField, ReferenceField, SequenceField, StringField
from mongoengine import CASCADE, PULL

from model.config import Config


class CustomDocument(Document):
    meta = {
        'abstract': True,
    }

    created_at = DateTimeField()
    updated_at = DateTimeField(default=datetime.datetime.now().replace(microsecond=0))

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.now().replace(microsecond=0)

        self.updated_at = datetime.datetime.now().replace(microsecond=0)
        return super(CustomDocument, self).save(*args, **kwargs)


class Member(CustomDocument):
    id_no = StringField(max_length=7, regex='\d{2}-\d{4}', required=True, primary_key=True)
    name = StringField(max_length=50, required=True)
    major = StringField(max_length=4, required=True)
    image = FileField(default=None)
    laptops = ListField(ReferenceField('Laptop'), default=None)

    @staticmethod
    def member_exists(member):
        return Member.objects(id_no=member.id_no).first() is not None

    def __eq__(self, other):
        return self.id_no == other.id_no

    def __repr__(self):
        return "%s - %s" % (self.id_no, self.name)


class Laptop(CustomDocument):
    serial_no = StringField(max_length=50, required=True, primary_key=True)
    make = StringField(max_length=10, required=True)
    owner = ReferenceField('Member')

    @staticmethod
    def laptop_exists(laptop):
        return Laptop.objects(serial_no__iexact=laptop.serial_no).first() is not None

    def __repr__(self):
        return "%s - %s" % (self.serial_no, self.make)


class Log(Document):
    index = SequenceField(primary_key=True)
    member = ReferenceField('Member')
    time_in = DateTimeField(default=datetime.datetime.now().replace(microsecond=0))
    time_out = DateTimeField(null=True, )

    # meta = {'collection': Config.collection}

    @staticmethod
    def get_members_in():
        members = []
        logs = Log.objects(time_out=None)

        for log in logs:
            members.append(log.member)

        return members


Laptop.register_delete_rule(Member, 'laptops', PULL)
Member.register_delete_rule(Laptop, 'owner', CASCADE)
