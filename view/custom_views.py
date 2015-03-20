'''
Created on Mar 13, 2015

@author: michael
'''

from PyQt5 import QtWidgets

class StyledMessageBox(QtWidgets.QMessageBox):
    '''
    classdocs
    '''
    
    def __init__(self, parent):
        QtWidgets.QMessageBox.__init__(self, parent)
        self.setStyleSheet("QWidget{\n"
"    background:white;\n"
"}\n"
"    QPushButton {\n"
"    background:-webkit-gradient(linear, left top, left bottom, color-stop(0.05, #599bb3),"
"    color-stop(1, #408c99));\n"
"    background:-moz-linear-gradient(top, #599bb3 5%, #408c99 100%);\n"
"    background:-webkit-linear-gradient(top, #599bb3 5%, #408c99 100%);\n"
"    background:-o-linear-gradient(top, #599bb3 5%, #408c99 100%);\n"
"    background:-ms-linear-gradient(top, #599bb3 5%, #408c99 100%);\n"
"    background:linear-gradient(to bottom, #599bb3 5%, #408c99 100%);\n"
"    background-color:#599bb3;\n"
"    border-radius:6px;\n"
"    border:1px solid #29668f;\n"
"    color:#ffffff;\n"
"    font-family:arial;\n"
"    font-size:15px;\n"
"    font-weight:bold;\n"
"    padding:6px 24px;\n"
"    text-decoration:none;\n"
"}\n"
"QPushButton:hover {\n"
"    background:-webkit-gradient(linear, left top, left bottom, color-stop(0.05, #408c99),"
"    color-stop(1, #599bb3));\n"
"    background:-moz-linear-gradient(top, #408c99 5%, #599bb3 100%);\n"
"    background:-webkit-linear-gradient(top, #408c99 5%, #599bb3 100%);\n"
"    background:-o-linear-gradient(top, #408c99 5%, #599bb3 100%);\n"
"    background:-ms-linear-gradient(top, #408c99 5%, #599bb3 100%);\n"
"    background:linear-gradient(to bottom, #408c99 5%, #599bb3 100%);\n"
"    background-color:#408c99;\n"
"}\n"
"QPushButton:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"}\n"
"QLabel{\n"
"    font-family:arial;\n"
"    font-size:15px;\n"
"    font-weight:bold;\n"
"    color:#599bb3;\n"
"    padding:6px 6px;\n"
"    text-decoration:none;\n"
"}\n"
"\n"
"\n"
"")
    def set_message(self, title, message):
        '''
        sets message and title for the messagebox
        '''
        self.setWindowTitle(title)
        self.setText(message)
        self.show()
        