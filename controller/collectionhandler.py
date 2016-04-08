import time
import datetime
from PyQt5 import QtCore
from mongoengine.context_managers import switch_collection

from model import Database
from model.config import Config
from model.do import Log


class CollectionHandler(QtCore.QObject):
    '''
    classdocs
    '''
    
    finished = QtCore.pyqtSignal()
    clean_up = QtCore.pyqtSignal()

    def __init__(self):
        super(CollectionHandler, self).__init__()
        self.__db = Database()
    
    @staticmethod
    def get_date():
        """
        Return current date
        """
        return datetime.datetime.today().strftime("%d%m%y")

    def change_collection(self):
        """
        Check every hour and change table if the day has changed
        """
        collection = '$' + self.get_date()

        if collection != Config.collection:
            Config.collection = collection
            self.clean_up.emit()

        time.sleep(3600)
        self.change_collection()
