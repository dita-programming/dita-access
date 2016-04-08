'''
Created on Mar 17, 2015

@author: michael
'''
from PyQt5 import QtCore
from mongoengine import connect

from controller.collectionhandler import CollectionHandler
from model import DAOFactory
from model.do import Log


class Startup(QtCore.QObject):
    """
    Handles the initial configuration and setup.

    This class restores any previous session(if any) and also initiates the background thread..
    """
    handler = CollectionHandler()
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
        self.handler.moveToThread(self.thread)
        self.handler.finished.connect(self.thread.quit)
        self.handler.clean_up.connect(self.__main.clean_up)
        self.thread.started.connect(self.handler.change_collection)
        self.thread.start()
        
    def load_previous_session(self):
        """
        Restores a previous session(if any).

        :return
        """
        members = Log.get_members_in()
        self.prev_session_loaded.emit(members)