'''
Created on Mar 17, 2015

@author: michael
'''
from PyQt5 import QtCore
from mongoengine import connect

from model.do import Log
from services.service import BackgroundService


class Startup(QtCore.QObject):
    """
    Handles the initial configuration and setup.

    This class restores any previous session(if any) and also initiates the background thread..
    """
    service = BackgroundService()
    thread = QtCore.QThread()
    prev_session_loaded = QtCore.pyqtSignal(list)

    def __init__(self, main):
        super(Startup, self).__init__()
        self.__main = main
        connect('dita_access')

    def start_thread(self):
        """
        Starts a background thread.

        :return
        """
        self.service.moveToThread(self.thread)
        self.service.finished.connect(self.thread.quit)
        self.service.clean_up.connect(self.__main.clean_up)
        self.thread.started.connect(self.service.reset)
        self.thread.start()
        
    def load_previous_session(self):
        """
        Restores a previous session(if any).

        :return
        """
        members = Log.get_members_in()
        self.prev_session_loaded.emit(members)