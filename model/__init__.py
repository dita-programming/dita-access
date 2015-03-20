"""
This is the main model.
"""
import mysql.connector
from model.config import SETTINGS


class Database():
    """
    This is the class of the model which handles all interactions
    with the database
    """    
    conn = mysql.connector.connect(**SETTINGS['db_config'])
    cursor = conn.cursor(buffered=True)
    
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
        cls.cursor.execute(query)
        
        
    @classmethod
    def set_table(cls, table):
        SETTINGS['table'] = '$' + table
        print(SETTINGS['table'])
    
    @classmethod
    def get_member(cls, id_no):
        """
        Return details of a member from the database
        """
        cls.cursor.execute("SELECT * FROM Members WHERE id=%s", (id_no,))
        return cls.cursor.fetchone()
     
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
    
    def __del__(self):
        self.conn.close()
    