#!/usr/bin/env python3
import sys
import datetime
from PyQt5 import QtCore, QtWidgets, QtGui
from view import Ui_MainWindow, StyledMessageBox, rc_dita
from controller import LaptopDialog, Center, Startup
from model import Database

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        Center(self)
        self.members_in_model = QtGui.QStandardItemModel(0, 1, self)
        self.members_in_model.setHeaderData(0, QtCore.Qt.Horizontal, "Members in")
        self.ui.treeView.setModel(self.members_in_model)
        self.members_in_ids = []
        self.members_in_names = []
        self.laptop = LaptopDialog(self)
        self.msg_box = StyledMessageBox(None)
        self.startup = Startup(self)
        self.startup.start_thread()
        QtCore.QTimer.singleShot(0, self.startup.load_previous_session)
        
    def closeEvent(self, event):
        """
        Intercept the close event in order to to destroy the
        background thread
        """
        self.startup.thread.quit()
        return QtWidgets.QMainWindow.closeEvent(self, event)
        
    @QtCore.pyqtSlot()
    def on_laptopButton_clicked(self):
        '''
        Slot to process laptopButton click
        '''
        self.laptop.reset()
        self.laptop.show()
        
    @QtCore.pyqtSlot()
    def on_idLineEdit_returnPressed(self):
        id_no = self.ui.idLineEdit.text()
        self.signout_member(id_no)
    
    @QtCore.pyqtSlot()
    def on_signoutButton_clicked(self):
        '''
        Slot to process signoutButton click
        '''
        id_no = self.ui.idLineEdit.text()
        self.signout_member(id_no)
        
    @QtCore.pyqtSlot()
    def on_adminButton_clicked(self):
        '''
        Slot to process adminButton click
        '''
        pass
            
    def signout_member(self, id_no):
        if not id_no:
            self.msg_box.set_message("Blank ID", "Please enter your student ID")
            return
        
        if self.check_member_in(id_no):
            Database.log_time_out(id_no, self.get_time())
            index = self.members_in_ids.index(id_no)
            name = self.members_in_names[index]
            self.members_in_model.removeRow(index)
            self.members_in_ids.remove(id_no)
            self.members_in_names.remove(name)
            self.msg_box.set_message("Goodbye", "Goodbye {}!".format(name))
        else:
            self.msg_box.set_message("Member", "{} hasn't signed in!".format(id_no))
            return

    def clean_up(self):
        """
        Cleans up current records on table change
        """
        self.members_in_ids.clear()
        self.members_in_names.clear()
        self.members_in_model.removeRows(0, self.members_in_model.rowCount())
        
    @classmethod
    def check_member_in(cls, id_no):        
        """
        Returns true if member is in and false if otherwise
        """
        if Database.get_member_log_details(id_no):
            return True
        else:
            return False
      
    @classmethod  
    def get_time(cls):
        """
        Returns current time
        """
        return datetime.datetime.now().time().replace(microsecond=0)
                
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
    