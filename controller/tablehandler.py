import time
import datetime
from PyQt5 import QtCore
from model import Database
from model.config import Config


class TableHandler(QtCore.QObject):
    '''
    classdocs
    '''
    
    finished = QtCore.pyqtSignal()
    clean_up = QtCore.pyqtSignal()

    def __init__(self):
        super(TableHandler, self).__init__()
        self.__db = Database()
    
    @staticmethod
    def get_date():
        """
        Return current date
        """
        return datetime.datetime.today().strftime("%d%m%y")
    
    def change_table(self):
        """
        Check every hour and change table if the day has changed
        """
        table_name = '$' + self.get_date()
        if table_name != Config.get_table():
            Config.set_table(table_name)
            self.__db.start_connection()
            self.__db.create_table(table_name)
            self.__db.close_connection()
            self.clean_up.emit()

        time.sleep(3600)
        self.change_table()