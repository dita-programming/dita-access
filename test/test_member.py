from unittest import TestCase

from mongoengine import connect

from model.do import Laptop, Member


__author__ = 'michael'


class TestMember(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        connect('access_test')

    def test_create(self):
        member = Member(id_no="77-7777", name="TestUser", major="ACS")
        member.save()

        member = Member.objects(id_no="77-7777").first()
        self.assertTrue(member, "List should not be empty")
        member.delete()

    def test_image(self):
        member = Member(id_no="77-7777", name="TestUser", major="ACS")

        with open('../resources/project.png', 'rb') as image:
            member.image.put(image)

        member.save()
        member = Member.objects(id_no="77-7777").first()
        self.assertIsNotNone(member.image.read(), "Image should not be None")
        member.delete()

    def test_laptop(self):
        member = Member(id_no="77-7777", name="TestUser", major="ACS")
        member.save()
        laptop = Laptop(serial_no="YYYYY", make="HP", owner=member)
        laptop.save()
        laptop = Laptop.objects(serial_no="YYYYY").first()
        self.assertEqual(member, laptop.owner, "Owner should be the same")
        member.delete()
        laptop.delete()

    def test_laptops(self):
        member = Member(id_no="77-7777", name="TestUser", major="ACS")
        member.save()
        laptop = Laptop(serial_no="YYYYY", make="HP", owner=member)
        laptop.save()
        laptop2 = Laptop(serial_no="ZZZZZ", make="DELL", owner=member)
        laptop2.save()
        member.update(add_to_set__laptops=[laptop, laptop2])
        member.reload()
        self.assertEqual(len(member.laptops), 2, "Should be 2")
        member.update(pull__laptops=laptop)
        member.reload()
        self.assertEqual(len(member.laptops), 1, "Should be 1")
        member.delete()
        laptop.delete()
        laptop2.delete()
