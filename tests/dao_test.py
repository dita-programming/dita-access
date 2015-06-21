import unittest
import datetime
from model import Database, DAOFactory
from model.dao import MemberDao, LogItemDao, LaptopDao
from model.member import Member
from model.laptop import Laptop
from model.log import LogItem


class TestDao(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = Database()
        cls.db.start_connection()
        cls.factory = DAOFactory(cls.db)

    def test_mbr_dao(self):
        dao = self.factory.get_dao("member")
        self.assertIsInstance(dao, MemberDao)
        self.assertEqual(len(dao.get_objects()), 2)
        m = Member("14-2000", "Jake")
        dao.add_object(m)
        self.assertEqual(len(dao.get_objects()), 3)
        dao.remove_object(m)
        self.assertEqual(len(dao.get_objects()), 2)

    def test_lpt_dao(self):
        dao = self.factory.get_dao("laptop")
        self.assertIsInstance(dao, LaptopDao)
        self.assertEqual(len(dao.get_objects()), 0)
        m = Member("14-2873", "Michael")
        l = Laptop("DELL", "BRF99N1", m)
        dao.add_object(l)
        self.assertEqual(len(dao.get_objects()), 1)
        dao.remove_object(l)
        self.assertEqual(len(dao.get_objects()), 0)

    def test_log_dao(self):
        dao = self.factory.get_dao("log")
        self.assertIsInstance(dao, LogItemDao)
        self.assertIsInstance(dao.get_incomplete_object("12"), LogItem)
        self.assertListEqual([], dao.get_incomplete_objects())
        m = Member("14-2873", "Michael")
        time = datetime.datetime.now().time().replace(microsecond=0).strftime("%H:%M")
        l = LogItem(m, time)
        dao.add_object(l)
        i_l = dao.get_incomplete_object("14-2873")
        self.assertEqual(i_l.member.id, m.id)
        time = datetime.datetime.now().time().replace(microsecond=0).strftime("%H:%M")
        i_l.time_out = time
        dao.update_object(i_l)

    @classmethod
    def tearDownClass(cls):
        cls.db.close_connection()
        del cls.factory
        del cls.db


if __name__ == '__main__':
    unittest.main()
