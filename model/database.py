from mongoengine import connect, ConnectionError
from model.config import Config


class Database:
    """
    Facilitates connections to the database
    """

    def __init__(self):
        self.__conn = None

    def start_connection(self):
        """
        Initiates a connection to the database.

        :return:
        """
        self.__conn = connect('access')

    @property
    def conn(self):
        return self.__conn

    @property
    def error(self):
        return
