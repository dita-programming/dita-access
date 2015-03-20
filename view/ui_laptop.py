# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'laptop.ui'
#
# Created: Thu Mar 19 21:56:12 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_laptopDialog(object):
    def setupUi(self, laptopDialog):
        laptopDialog.setObjectName("laptopDialog")
        laptopDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        laptopDialog.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(laptopDialog.sizePolicy().hasHeightForWidth())
        laptopDialog.setSizePolicy(sizePolicy)
        laptopDialog.setStyleSheet("QDialog {\n"
"    background: white;\n"
"    border: 1px solid #29668f;\n"
"}\n"
"QPushButton {\n"
"    background:-webkit-gradient(linear, left top, left bottom, color-stop(0.05, #599bb3), color-stop(1, #408c99));\n"
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
"    background:-webkit-gradient(linear, left top, left bottom, color-stop(0.05, #408c99), color-stop(1, #599bb3));\n"
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
"QLineEdit {\n"
"    border-radius:6px;\n"
"    border:1px solid #29668f;\n"
"    font-weight:bold;\n"
"    padding:6px 24px;\n"
"}\n"
"QLineEdit:Disabled{\n"
"    border-radius:6px;\n"
"    border:1px solid #333333;\n"
"    font-weight:bold;\n"
"    padding:6px 24px;\n"
"    background: #808080;\n"
"}\n"
"QLabel{\n"
"    font-family:arial;\n"
"    font-size:15px;\n"
"    font-weight:bold;\n"
"    color:#599bb3;\n"
"    padding:6px 6px;\n"
"    text-decoration:none;\n"
"}\n"
"QCheckBox{\n"
"    font-family:arial;\n"
"    font-size:15px;\n"
"    font-weight:bold;\n"
"    color:#599bb3;\n"
"    padding:6px 6px;\n"
"    text-decoration:none;\n"
"}\n"
"\n"
"")
        self.gridLayout_3 = QtWidgets.QGridLayout(laptopDialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(laptopDialog)
        self.checkBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.serialLineEdit = QtWidgets.QLineEdit(laptopDialog)
        self.serialLineEdit.setObjectName("serialLineEdit")
        self.gridLayout.addWidget(self.serialLineEdit, 0, 1, 1, 1)
        self.idLineEdit = QtWidgets.QLineEdit(laptopDialog)
        self.idLineEdit.setObjectName("idLineEdit")
        self.gridLayout.addWidget(self.idLineEdit, 1, 1, 1, 1)
        self.lb_id = QtWidgets.QLabel(laptopDialog)
        self.lb_id.setObjectName("lb_id")
        self.gridLayout.addWidget(self.lb_id, 1, 0, 1, 1)
        self.lb_serial = QtWidgets.QLabel(laptopDialog)
        self.lb_serial.setObjectName("lb_serial")
        self.gridLayout.addWidget(self.lb_serial, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 1, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem4, 2, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(laptopDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_3.addWidget(self.buttonBox, 3, 1, 1, 1)

        self.retranslateUi(laptopDialog)
        self.buttonBox.accepted.connect(laptopDialog.accept)
        self.buttonBox.rejected.connect(laptopDialog.reject)
        self.checkBox.toggled['bool'].connect(self.serialLineEdit.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(laptopDialog)

    def retranslateUi(self, laptopDialog):
        _translate = QtCore.QCoreApplication.translate
        laptopDialog.setWindowTitle(_translate("laptopDialog", "Laptop Dialog"))
        self.checkBox.setText(_translate("laptopDialog", "No laptop ?"))
        self.lb_id.setText(_translate("laptopDialog", "ID No."))
        self.lb_serial.setText(_translate("laptopDialog", "Serial No."))

