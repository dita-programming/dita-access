'''
Created on Mar 17, 2015

@author: michael
'''
import time
import datetime
from PyQt5 import QtCore
from model import Database
from model.config import SETTINGS

class TableHandler(QtCore.QObject):
    '''
    classdocs
    '''
    
    finished = QtCore.pyqtSignal()
    
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
        if table_name != SETTINGS['table']:
            SETTINGS['table'] = table_name
            Database.create_table(table_name)
                
                    
        time.sleep(3600)
        self.change_table()
                
