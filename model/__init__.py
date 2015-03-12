import mysql.connector

class Model():
    
    config = {"user":"root",
              "password":"root",
              "host":"localhost",
              "database":"dita"}
    
    table = None
    
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor(buffered=True)
    
    def create_table(self,table):
        self.table = '$' + table
        query = """CREATE TABLE %s (
                    id VARCHAR(10) NOT NULL,
                    time_in DATETIME NOT NULL,
                    time_out DATETIME NULL,
                    PRIMARY KEY(id));""" % self.table
        self.cursor.execute(query)
    
    def get_user(self,id_no):
        self.cursor.execute("SELECT * FROM %s WHERE id=%s",(self.table,id_no))
    
    def get_laptop(self,serial_no):
        self.cursor.execute("SELECT * FROM Laptops WHERE serial=%s",(serial_no,))
    
    def log_time_in(self,id_no,time_in):
        self.cursor.execute("INSERT INTO %s(id,time_in) VALUES(%s,%s)",(self.table,id_no,time_in))
    
    def log_time_out(self,id_no,time_out):
        self.cursor.execute("UPDATE %s SET time_out=%s WHERE id=%s AND time_out IS NULL",
                            (self.table,id_no,time_out))