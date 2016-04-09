import csv

from mongoengine import connect
from mongoengine.connection import get_connection

from model.do import Member, Laptop

MEMBERS = []

connect('dita_access')
connection = get_connection()
connection.drop_database('dita_access')

with open('members.csv', 'r') as members_file:
    reader = csv.reader(members_file)
    rows = [row for row in reader]
    rows.pop(0)

    for row in rows:
        member = Member(id_no=row[0], name=row[1])
        MEMBERS.append(member)

with open('acs_mis.csv', 'r') as students_file:
    reader = csv.reader(students_file)
    rows = [row for row in reader]
    rows.pop(0)

    print("Importing members")
    for member in MEMBERS:
        for row in rows:
            if row[1].strip() == member.id_no:
                if row[3].strip() == "BSc Applied Computer Science":
                    member.major = 'ACS'
                elif row[3].strip() == "B Com Management Information Systems":
                    member.major = 'MIS'
        member.save()

with open('laptops.csv', 'r') as laptops_file:
    reader = csv.reader(laptops_file)
    rows = [row for row in reader]
    rows.pop(0)

    print("Importing laptops")
    for row in rows:
        laptop = Laptop(serial_no=row[0].upper(), make=row[1].upper())
        for member in MEMBERS:
            if member.id_no == row[2]:
                laptop.owner = member

        laptop.save()

print("Import complete")
