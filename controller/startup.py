'''
Created on Mar 17, 2015

@author: michael
'''
from PyQt5 import QtCore
from controller.tablehandler import TableHandler
from model import DAOFactory


class Startup(QtCore.QObject):
    """
    Handles the initial configuration and setup.

    This class restores any previous session(if any) and also initiates the background thread..
    """
    handler = TableHandler()
    thread = QtCore.QThread()
    prev_session_loaded = QtCore.pyqtSignal(list)

    def __init__(self, main, db):
        super(Startup, self).__init__()
        self.__main = main
        self.__db = db
        self.__db.start_connection()
        self.__db.create_tables()
        self.__db.close_connection()
        
    def start_thread(self):
        """
        Starts a background thread.

        :return
        """
        self.handler.moveToThread(self.thread)
        self.handler.finished.connect(self.thread.quit)
        self.handler.clean_up.connect(self.__main.clean_up)
        self.thread.started.connect(self.handler.change_table)
        self.thread.start()
        
    def load_previous_session(self):
        """
        Restores a previous session(if any).

        :return
        """
        self.__db.start_connection()
        log_dao = DAOFactory(self.__db).get_dao("log")
        log = log_dao.get_incomplete_objects()
        self.__db.close_connection()
        members = [log_item.member for log_item in log]
        self.prev_session_loaded.emit(members)