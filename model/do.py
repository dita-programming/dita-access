from mongoengine import Document, FileField, ListField, ReferenceField, StringField, CASCADE, PULL


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


Laptop.register_delete_rule(Member, 'laptops', PULL)
Member.register_delete_rule(Laptop, 'owner', CASCADE)
