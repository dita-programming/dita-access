from abc import ABCMeta, abstractmethod
from model.member import Member
from model.laptop import Laptop
from model.log import LogItem
from model.config import Config


class DAOFactory:
    def __init__(self, db):
        self.__db = db

    @property
    def connection(self):
        return self.__db

    @connection.setter
    def connection(self, db):
        self.__db = db

    def get_dao(self, val):
        dao = val

        if dao is None:
            return None

        if dao.lower() == "member":
            return MemberDao(self.__db)
        elif dao.lower() == "laptop":
            return LaptopDao(self.__db)
        elif dao.lower() == "log":
            return LogItemDao(self.__db)


class BaseDao(metaclass=ABCMeta):
    def __init__(self, db):
        self._db = db

    @abstractmethod
    def add_object(self, obj):
        pass

    @abstractmethod
    def remove_object(self, obj):
        pass

    @abstractmethod
    def update_object(self, obj):
        pass

    @abstractmethod
    def get_object(self, key):
        pass

    @abstractmethod
    def get_objects(self):
        pass


class MemberDao(BaseDao):
    def __init__(self, db=None):
        super(MemberDao, self).__init__(db)

    def add_object(self, obj):
        """Persists a Member instance.

        Adds the details of a Member instance to the database.
        :param obj: A member instance to be added
        :return:
        """
        try:
            self._db.cursor.execute("INSERT INTO Members VALUES(%s,%s)", (obj.id, obj.name))
            self._db.conn.commit()
        except self._db.error:
            print("Unable to add member")

    def remove_object(self, obj):
        """Removes a persisted Member instance

        Removes the details of a Member instance from the database.
        :param obj: A Member instance to be removed
        :return:
        """
        try:
            self._db.cursor.execute("DELETE FROM Members WHERE id_no=%s", (obj.id,))
            self._db.conn.commit()
        except self._db.error:
            print("Unable to delete member")

    def update_object(self, obj):
        pass

    def get_object(self, id_no):
        """Returns a Member instance

        Returns a Member instance with the details fetched of a member fetched from
        the database.
        :param id_no: A string with the member id to fetch
        :return: A member instance with the fetched details
        """
        m = Member()
        try:
            self._db.cursor.execute("SELECT * FROM Members WHERE id_no=%s", (id_no,))
            details = self._db.cursor.fetchone()
            m.id = details[0]
            m.name = details[1]
        except self._db.error:
            print("Member not found")
        finally:
            return m

    def get_objects(self):
        try:
            members = []

            self._db.cursor.execute("SELECT * FROM Members")
            if self._db.cursor.with_rows:
                members = [Member(row) for row in self._db.cursor.fetchall()]
        except self._db.error:
            print("No member found")
        finally:
            return members


class LaptopDao(BaseDao):
    def __init__(self, db=None):
        super(LaptopDao, self).__init__(db)

    def add_object(self, obj):
        """Persists a Laptop instance.

        Adds the details of a Laptop instance to the database.
        :param obj: A Laptop instance to be added
        :return:
        """
        try:
            self._db.cursor.execute("INSERT INTO Laptops VALUES(%s,%s,%s)", (obj.make, obj.serial, obj.member.id))
            self._db.conn.commit()
        except self._db.error:
            print("Unable to add laptop")

    def remove_object(self, obj):
        """Removes a persisted Laptop instance

        Removes the details of a Laptop instance from the database.
        :param obj: A Laptop instance to be removed
        :return:
        """
        try:
            self._db.cursor.execute("DELETE FROM Laptops WHERE serial=%s", (obj.serial,))
            self._db.conn.commit()
        except self._db.error:
            print("Unable to delete laptop")

    def update_object(self, obj):
        pass

    def get_object(self, serial):
        """Returns a Laptop instance

        Returns a Laptop instance with the details fetched of a laptop fetched from
        the database.
        :param id_no: A string with the laptop serial to fetch
        :return: A Laptop instance with the fetched details
        """
        l = Laptop()
        try:
            self._db.cursor.execute("SELECT * FROM Laptops WHERE lower(serial)=%s", (serial.lower(),))
            details = self._db.cursor.fetchone()
            l.serial = details[0]
            l.make = details[1]
            l.member = DAOFactory(self._db).get_dao("member").get_object(details[2])
        except self._db.error:
            print("Laptop not found")
        finally:
            return l

    def get_objects(self):
        try:
            laptops = []

            self._db.cursor.execute("SELECT * FROM Laptops")
            if self._db.cursor.with_rows:
                laptops = [Laptop(row) for row in self._db.cursor.fetchall()]
        except self._db.error:
            print("No laptop found")
        finally:
            return laptops


class LogItemDao(BaseDao):
    def __init__(self, db=None):
        super(LogItemDao, self).__init__(db)

    def add_object(self, obj):
        """Persists a LogItem instance.

        Adds the details of a LogItem instance to the database.
        :param obj: A LogItem instance to be added
        :return:
        """
        try:
            query = "INSERT INTO {}(id_no, time_in) VALUES(%s,%s)".format(Config.get_table())
            self._db.cursor.execute(query, (obj.member.id, obj.time_in))
            self._db.conn.commit()
        except self._db.error:
            print("Unable to log time in")

    def remove_object(self, obj):
        pass

    def update_object(self, obj):
        """Persists a LogItem instance.

        Updates the details of a LogItem instance to the database.
        :param obj: A LogItem instance to be updated
        :return:
        """
        try:
            query = "UPDATE {} SET time_out=%s WHERE id_no=%s AND time_out IS NULL".format(Config.get_table())
            self._db.cursor.execute(query, (obj.time_out, obj.member.id))
            self._db.conn.commit()
        except self._db.error:
            print("Unable to log time out")

    def get_object(self, key):
        pass

    def get_objects(self):
        """Returns the entire log

        :return: A list of LogItem instances
        """
        try:
            log_items = []

            self._db.cursor.execute("SELECT * FROM {}".format(Config.get_table()))
            result = self._db.cursor.fetchall()
            if result:
                mbr_dao = DAOFactory(self._db).get_dao("member")
                for row in result:
                    log_items.append(LogItem(mbr_dao.get_object(row[1]), row[2], row[3]))
        except self._db.error:
            print("get_objects(): No log item found")
        finally:
            return log_items

    def get_incomplete_object(self, id_no):
        try:
            l = LogItem()
            query = "SELECT * FROM {} WHERE id_no=%s AND time_out IS NULL".format(Config.get_table())
            self._db.cursor.execute(query, (id_no,))
            result = self._db.cursor.fetchone()
            if result:
                l.member = DAOFactory(self._db).get_dao("member").get_object(result[1])
                l.time_in = result[2]
                l.time_out = result[3]
        except self._db.error:
            print("get_incomplete_object(): No log item found")
        finally:
            return l

    def get_incomplete_objects(self):
        """Returns incomplete log items

        :return: A list of LogItem instances
        """
        try:
            log_items = []
            query = "SELECT * FROM {} WHERE time_out IS NULL".format(Config.get_table())
            self._db.cursor.execute(query)

            result = self._db.cursor.fetchall()
            if result:
                mbr_dao = DAOFactory(self._db).get_dao("member")
                for row in result:
                    log_items.append(LogItem(mbr_dao.get_object(row[1]), row[2], row[3]))
        except self._db.error:
            print("get_incomplete_objects(): No log item found")
        finally:
            return log_items

