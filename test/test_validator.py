import unittest

from mongoengine import connect
from mongoengine.connection import get_connection

from model import ValidatorFactory, Config
from model.do import Member, Laptop, Log


class TestValidator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        connect('access_test')
        Config.collection = "test"

    def tearDown(self):
        connection = get_connection()
        connection.drop_database('access_test')

    def test_sign_in_without_laptop(self):
        member = Member(id_no="77-7777", name="TestUser", major="ACS")
        laptop = Laptop()
        validator = ValidatorFactory(member, laptop).get_validator("sign in")
        self.assertEqual(validator.validate(), False)
        member.save()

        validator.no_laptop_checked = True
        self.assertEqual(validator.validate(), True)

        log = Log(member=member)
        log.save()

        self.assertEqual(validator.validate(), False)

    def test_sign_in_with_laptop(self):
        member = Member(id_no="77-7777", name="TestUser", major="ACS")
        member.save()
        member2 = Member(id_no="88-8888", name="TestUser", major="MIS")
        member2.save()
        laptop = Laptop(serial_no="YYYYY", make="ZZZ", owner=member)
        laptop.save()
        validator = ValidatorFactory(member2, laptop).get_validator("sign in")
        self.assertEqual(validator.validate(), False)

        validator = ValidatorFactory(member, laptop).get_validator("sign in")
        self.assertEqual(validator.validate(), True)

    def test_sign_out(self):
        member = Member(id_no="77-7777", name="TestUser", major="ACS")
        member.save()
        laptop = Laptop()
        validator = ValidatorFactory(member, laptop).get_validator("sign out")
        self.assertEqual(validator.validate(), False)

        log = Log(member=member)
        log.save()
        self.assertEqual(validator.validate(), True)


if __name__ == '__main__':
    unittest.main()
