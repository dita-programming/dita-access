'''
Created on Mar 17, 2015

@author: michael
'''
from PyQt5 import QtWidgets
from view import Ui_laptopDialog, StyledMessageBox
from model import Database

class LaptopDialog(QtWidgets.QDialog):
    
    def __init__(self, parent):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = Ui_laptopDialog()
        self.ui.setupUi(self)
        self.model = self.parent().members_in_model
        self.msg_box = StyledMessageBox(None)
    
    def reset(self):
        """
        Reset the dialog box for new input
        """
        self.ui.idLineEdit.clear()
        self.ui.serialLineEdit.clear()
        self.ui.checkBox.setChecked(False)
        
    def accept(self):
        login = False
        id_no = self.ui.idLineEdit.text()
        serial_no = self.ui.serialLineEdit.text().lower()
        
        if not serial_no and not self.ui.checkBox.isChecked():
            self.msg_box.set_message("Blank Serial", "Please enter your laptop's serial No.")
            return
        
        if not id_no:
            self.msg_box.set_message("Blank ID", "Please enter your student ID")
            return
        
        if Database.check_member_exists(id_no):
            if self.parent().check_member_in(id_no):
                self.msg_box.set_message("Member", "{} has already signed in!".format(id_no))                  
            else:
                if not self.ui.checkBox.isChecked():
                    if Database.check_laptop_exists(serial_no):
                        if Database.get_laptop(serial_no)[2] == id_no:
                            login = True
                        else:
                            self.msg_box.set_message("Duplicate Laptop", 
                                                     "Laptop registered to another member!")
                    else:
                        self.msg_box.set_message("Unregistered Laptop", "Laptop not registered!")
                else:
                    login = True
        else:
            self.msg_box.set_message("Unregistered Member", "{} not registered!".format(id_no))
            return    
        
        
        if login:
            name = Database.get_member(id_no)[1].split()[0].title()
            name_id = "{} ({})".format(name, id_no)
            Database.log_time_in(id_no, self.parent().get_time())   
            self.parent().members_in_ids.append(id_no)
            self.parent().members_in_names.append(name)
            index = self.parent().members_in_ids.index(id_no)
            self.model.insertRow(index)
            self.model.setData(self.model.index(index, 0), name_id)       
            self.msg_box.set_message("Welcome", "Welcome {}!".format(name))
            return QtWidgets.QDialog.accept(self)  
        else:
            return
            