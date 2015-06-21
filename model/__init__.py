"""
This is the main model.
"""
from model.database import Database
from model.member import Member
from model.laptop import Laptop
from model.log import LogItem
from model.dao import DAOFactory
from model.validator import ValidatorFactory
from model.config import Config


'''class Database():
    """
    This is the class of the model which handles all interactions
    with the database
    """
    db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
    db.setHostName(SETTINGS['db_config']['host'])
    db.setDatabaseName(SETTINGS['db_config']['database'])
    db.setUserName(SETTINGS['db_config']['user'])
    db.setPassword(SETTINGS['db_config']['password'])
    db.open()
    #conn = mysql.connector.connect(**SETTINGS['db_config'])
    cursor = QtSql.QSqlQuery(db)
    
    @classmethod
    def create_table(cls, table):
        """
        Create a new table in the database if it doesn't exist
        """
        query = """CREATE TABLE IF NOT EXISTS %s (
                    indx INTEGER NOT NULL AUTO_INCREMENT,
                    id VARCHAR(10) NOT NULL,
                    time_in TIME NOT NULL,
                    time_out TIME NULL,
                    PRIMARY KEY(indx))
                    ;""" % (table)
        cls.cursor.exec_(query)
        
        
    @classmethod
    def set_table(cls, table):
        SETTINGS['table'] = '$' + table
        print(SETTINGS['table'])
    
    @classmethod
    def get_member(cls, id_no):
        """
        Return details of a member from the database
        """
        cls.cursor.prepare("SELECT * FROM Members WHERE id=?")
        cls.cursor.addBindValue(id_no)
        cls.cursor.exec_()

        if cls.cursor.next():
            return cls.cursor
        else:
            return None
     
    @classmethod   
    def check_member_exists(cls, id_no):
        """
        Return true if a member exists in the database and false otherwise
        """
        cls.cursor.execute("SELECT * FROM Members WHERE id=%s", (id_no,))
        if cls.cursor.fetchone():
            return True
        else:
            return False
    
    @classmethod
    def get_laptop(cls, serial_no):
        """
        Return the details of a laptop in the database
        """
        cls.cursor.execute("SELECT * FROM Laptops WHERE serial=%s", (serial_no,))
        return cls.cursor.fetchone()
    
    @classmethod
    def check_laptop_exists(cls, serial_no):
        """
        Return true if laptop exists in the database and false if it doesn't
        """
        cls.cursor.execute("SELECT * FROM Laptops WHERE serial=%s", (serial_no,))
        if cls.cursor.fetchone():
            return True
        else:
            return False
    
    @classmethod
    def log_time_in(cls, id_no, time_in):
        """
        Log the time in of a member into the database
        """
        query = "INSERT INTO {}(id,time_in) VALUES(%s,%s)".format(SETTINGS['table'])
        
        cls.cursor.execute(query, (id_no, time_in))
        cls.conn.commit()
    
    @classmethod
    def log_time_out(cls, id_no, time_out):
        """
        Log the time out of a member into the database
        """
        query = "UPDATE {} SET time_out=%s WHERE id=%s AND time_out IS NULL".format(SETTINGS['table'])
        cls.cursor.execute(query, (time_out, id_no))
        cls.conn.commit()
   
    @classmethod     
    def get_member_log_details(cls, id_no):
        """
        Return log details of a particular member
        """
        query = "SELECT * FROM {} WHERE id=%s AND time_out IS NULL".format(SETTINGS['table'])
        cls.cursor.execute(query, (id_no,))
        return cls.cursor.fetchone()
    
    @classmethod
    def get_members_in(cls):
        """
        Return a list of members in
        """
        if SETTINGS['table'] == None:
            return None
        else:
            query = "SELECT id FROM {} WHERE time_out IS NULL".format(SETTINGS['table'])
            cls.cursor.execute(query)
        return cls.cursor.fetchall()

    @classmethod
    def store_records(cls, date, records):
        """
        Stores the records of the day if any
        """
        cls.cursor.execute("INSERT INTO Records(date,ids)",(date,records))
        cls.conn.commit()


    def __del__(self):
        conn_name = self.db.connectionName()
        self.db.removeDatabase(conn_name)


db = Database()
db.create_table("Members")
#print(db.get_member('14-2807'))'''