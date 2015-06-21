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

    '''def create_tables(self):
        """
        Creates the required tables in the database.

        :return:
        """
        self.__start_connection()
        self.__cursor.exec_("""CREATE TABLE IF NOT EXISTS Members(
                            id_no VARCHAR(10) NOT NULL,
                            name VARCHAR(30) NOT NULL,
                            PRIMARY KEY(id_no))""")

        self.__cursor.exec_("""CREATE TABLE IF NOT EXISTS Laptops(
                            make VARCHAR(10) NOT NULL,
                            serial VARCHAR(20) NOT NULL,
                            id_no VARCHAR(10) NOT NULL
                            PRIMARY KEY(serial))""")
        print("Tables created")

        self.__close_connection()

    def get_member(self, id_no):
        """
        Returns details of a member from the database.

        :param id_no: A string representing a key of which row to fetch
        :return: A Member instance with the details fetched.
        """
        m = Member()
        self.__start_connection()
        self.__cursor.prepare("SELECT * FROM Members WHERE id=?")
        self.__cursor.addBindValue(id_no)
        self.__cursor.exec_()

        if self.__cursor.next():
            m.name = self.__cursor.value(0)
            m.id = self.__cursor.value(1)

        self.__close_connection()
        return m

    def get_members_in(self):
        """
        Return a list of members in.

        :return: A list of Member instances.
        """
        if SETTINGS['table'] is None:
            return []
        else:
            members_list = []
            self.__start_connection()
            query = "SELECT id FROM {} WHERE time_out IS NULL".format(SETTINGS['table'])
            self.__cursor.exec_(query)
            while self.__cursor.next():
                members_list.append(self.get_member(self.__cursor.value(1)))

            return members_list

    def get_laptop(self, serial_no):
        """
        Return the details of a laptop in the database

        :param serial_no: A string representing a key of which row to fetch
        :return: A Laptop instance with the details fetched.
        """
        l = Laptop()
        self.__start_connection()
        self.__cursor.prepare("SELECT * FROM Laptops WHERE serial=?")
        self.__cursor.addBindValue(serial_no)
        self.__cursor.exec_()

        if self.__cursor.next():
            l.make = self.__cursor.value(0)
            l.serial = self.__cursor.value(1)
            l.member = self.get_member(self.__cursor.value(2))

        self.__close_connection()
        return l








class Log:

    def __init__(self):
        pass'''
