import mysql.connector
from model.config import Config


class Database:
    """

    """

    def __init__(self):
        self.__conn = None
        self.__cursor = None

    def start_connection(self):
        """
        Initiates a connection to the database.

        :return:
        """
        self.__conn = mysql.connector.connect(**Config.db_config)
        self.__cursor = self.__conn.cursor(buffered=True)

    def close_connection(self):
        """
        Closes the connection to the database.

        :return:
        """
        if self.__cursor:
            self.__cursor.close()
        if self.__conn:
            self.__conn.close()

    def create_table(self, table_name):
        query = """CREATE TABLE IF NOT EXISTS {} (
                    indx INTEGER NOT NULL AUTO_INCREMENT,
                    id_no VARCHAR(10) NOT NULL,
                    time_in TIME NOT NULL,
                    time_out TIME NULL,
                    PRIMARY KEY(indx));""".format(table_name)
        self.__cursor.execute(query)

    def create_tables(self):
        self.__cursor.execute("""CREATE TABLE IF NOT EXISTS Members(
                              id_no VARCHAR(10) NOT NULL,
                              name VARCHAR(30) NOT NULL,
                              PRIMARY KEY(id_no))""")

        self.__cursor.execute("""CREATE TABLE IF NOT EXISTS Laptops(
                              make VARCHAR(10) NOT NULL,
                              serial VARCHAR(20) NOT NULL,
                              id_no VARCHAR(10) NOT NULL,
                              PRIMARY KEY(serial))""")

    @property
    def conn(self):
        return self.__conn

    @property
    def cursor(self):
        return self.__cursor

    @property
    def error(self):
        return mysql.connector.Error

   