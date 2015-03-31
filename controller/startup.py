'''
Created on Mar 17, 2015

@author: michael
'''
from PyQt5 import QtCore
from controller.tablehandler import TableHandler
from model import Database

class Startup():
    '''
    This class handles the initial configurations and also starts the 
    background thread.
    '''
    handler = TableHandler()
    thread = QtCore.QThread()
    
    def __init__(self, main):
        self.main = main
        self.model = main.members_in_model
        
    def start_thread(self):
        '''
        Start background thread
        '''
        self.handler.moveToThread(self.thread)
        self.handler.finished.connect(self.thread.quit)
        self.handler.clean_up.connect(self.main.clean_up)
        self.thread.started.connect(self.handler.change_table)
        self.thread.start()
        
    def load_previous_session(self):
        '''
        Load previous session if program exited program exited
        abruptly
        '''
        members = Database.get_members_in()
        if members:
            for member in members:
                name = Database.get_member(member[0])[1].split()[0].title()
                name_id = "{} ({})".format(name, member[0])
                self.main.members_in_ids.append(member[0])
                self.main.members_in_names.append(name)
                index = self.main.members_in_ids.index(member[0])
                self.model.insertRow(index)
                self.model.setData(self.model.index(index, 0), name_id)
                