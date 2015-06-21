import unittest
from model import Database, DAOFactory, ValidatorFactory
from model.validator import SignInValidator, SignOutValidator


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = Database()
        cls.db.start_connection()
        factory = DAOFactory(cls.db)
        mbr_dao = factory.get_dao("member")
        lpt_dao = factory.get_dao("laptop")
        log_dao = factory.get_dao("log")
        cls.val_factory = ValidatorFactory(mbr_dao, lpt_dao, log_dao, None, None)

    def test_sig_in(self):
        validator = self.val_factory.get_validator("sign in")
        self.assertIsInstance(validator, SignInValidator)

    def test_sign_out(self):
        validator = self.val_factory.get_validator("sign out")
        self.assertIsInstance(validator, SignOutValidator)

    @classmethod
    def tearDownClass(cls):
        cls.db.close_connection()
        del cls.val_factory


if __name__ == '__main__':
    unittest.main()
