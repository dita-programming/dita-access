import sys
import datetime
from PyQt5 import QtCore, QtWidgets, QtGui
from view import Ui_MainWindow, Ui_laptopDialog, StyledMessageBox, rc_dita
from controller import Center, TableHandler
from model import Database

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        Center(self)
        self.db = Database()
        self.members_in_model = QtGui.QStandardItemModel(0,1,self)
        self.members_in_model.setHeaderData(0,QtCore.Qt.Horizontal,"Members in")
        self.ui.treeView.setModel(self.members_in_model)
        self.members_in_ids = []
        self.members_in_names = []
        
        # Setup second thread to check the date continuously
        # in order to change model log table
        self.thread = QtCore.QThread()
        self.tables = TableHandler(self)
        self.tables.moveToThread(self.thread)
        self.tables.finished.connect(self.thread.quit)
        self.thread.started.connect(self.tables.change_table)
        self.thread.start()
        
    @QtCore.pyqtSlot()
    def on_laptopButton_clicked(self):
        self.laptop = LaptopDialog(self)
        self.laptop.show()
        
    @QtCore.pyqtSlot()
    def on_idLineEdit_returnPressed(self):
        id_no = self.ui.idLineEdit.text()
        self.signout_member(id_no)
    
    @QtCore.pyqtSlot()
    def on_signoutButton_clicked(self):
        id_no = self.ui.idLineEdit.text()
        self.signout_member(id_no)
        
    @QtCore.pyqtSlot()
    def on_adminButton_clicked(self):
        pass
            
    def signout_member(self,id_no):
        if not id_no:
            self.msg_box = StyledMessageBox(None, "Blank ID", "Please enter your student ID")
            self.msg_box.show()
            return
        
        if self.check_member_in(id_no):
            self.db.log_time_out(id_no, self.get_time())
            index = self.members_in_ids.index(id_no)
            name = self.members_in_names[index]
            self.members_in_model.removeRow(index)
            self.members_in_ids.remove(id_no)
            self.members_in_names.remove(name)
            self.msg_box = StyledMessageBox(None, "Goodbye", "Goodbye {}!".format(name))
            self.msg_box.show()
        else:
            self.msg_box = StyledMessageBox(None, "Member", "{} hasn't signed in!".format(id_no))
            self.msg_box.show()
            return
        
    def check_member_in(self,id_no):
        result = self.db.get_member_log_details(id_no)
        
        if result:
            return True
        else:
            return False
        
    def get_time(self):
        time = datetime.datetime.now().time().replace(microsecond=0)
        return time
        
class LaptopDialog(QtWidgets.QDialog):
    
    def __init__(self,parent):
        QtWidgets.QDialog.__init__(self,parent)
        self.ui = Ui_laptopDialog()
        self.ui.setupUi(self)
        self.db = self.parent().db
        self.model = self.parent().members_in_model
        
    def accept(self):
        id_no = self.ui.idLineEdit.text()
        serial_no = self.ui.serialLineEdit.text().lower()
        
        if not serial_no:
            self.msg_box = StyledMessageBox(None, "Blank Serial", "Please enter your laptop's serial No.")
            self.msg_box.show()
            return
        
        if not id_no:
            self.msg_box = StyledMessageBox(None, "Blank ID", "Please enter your student ID")
            self.msg_box.show()
            return
        
        if self.db.check_member_exists(id_no):        
            if self.db.check_laptop_exists(serial_no):
                if self.db.get_laptop(serial_no)[2] == id_no:
                    name = self.db.get_member(id_no)[1].split()[0].title()
                    name_id = "{} ({})".format(name,id_no)
                    
                    if self.parent().check_member_in(id_no):
                        self.msg_box = StyledMessageBox(None, "Member", "{} has already signed in!".format(id_no))
                        self.msg_box.show()                  
                        return                        
                    else:
                        self.db.log_time_in(id_no, self.parent().get_time())   
                        self.parent().members_in_ids.append(id_no)
                        self.parent().members_in_names.append(name)
                        index =  self.parent().members_in_ids.index(id_no)
                        self.model.insertRow(index)
                        self.model.setData(self.model.index(index,0),name_id)       
                        self.msg_box = StyledMessageBox(None, "Welcome", "Welcome {}!".format(name))
                        self.msg_box.show()
                        return QtWidgets.QDialog.accept(self)  
                else:
                    self.msg_box = StyledMessageBox(None, "Duplicate Laptop", "Laptop registered to another member!")
                    self.msg_box.show()
                    return           
            else:
                self.msg_box = StyledMessageBox(None, "Unregistered Laptop", "Laptop not registered!")
                self.msg_box.show()
                return   
        else:
            self.msg_box = StyledMessageBox(None, "Unregistered Member", "{} not registered!".format(id_no))
            self.msg_box.show()
            return
                
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())