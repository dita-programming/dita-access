# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sign_in.ui'
#
# Created: Mon Jun 22 00:34:42 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sign_inDialog(object):
    def setupUi(self, sign_inDialog):
        sign_inDialog.setObjectName("sign_inDialog")
        sign_inDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        sign_inDialog.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(sign_inDialog.sizePolicy().hasHeightForWidth())
        sign_inDialog.setSizePolicy(sizePolicy)
        sign_inDialog.setStyleSheet("QDialog {\n"
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
"QLineEdit:disabled {\n"
"    background: #8C8C8C;\n"
"    border-radius:6px;\n"
"    border:1px solid #29668f;\n"
"    font-weight:bold;\n"
"    padding:6px 24px;\n"
"}\n"
"QLabel{\n"
"    font-family:arial;\n"
"    font-size:15px;\n"
"    font-weight:bold;\n"
"    color:#599bb3;\n"
"    padding:6px 6px;\n"
"    text-decoration:none;\n"
"}\n"
"QLabel:disabled{\n"
"    font-family:arial;\n"
"    font-size:15px;\n"
"    font-weight:bold;\n"
"    color:grey;\n"
"    padding:6px 6px;\n"
"    text-decoration:none;\n"
"}\n"
"\n"
"QCheckBox{\n"
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
        self.gridLayout_2 = QtWidgets.QGridLayout(sign_inDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.txt_serial = QtWidgets.QLineEdit(sign_inDialog)
        self.txt_serial.setEnabled(True)
        self.txt_serial.setObjectName("txt_serial")
        self.gridLayout.addWidget(self.txt_serial, 0, 1, 1, 1)
        self.txt_id = QtWidgets.QLineEdit(sign_inDialog)
        self.txt_id.setObjectName("txt_id")
        self.gridLayout.addWidget(self.txt_id, 1, 1, 1, 1)
        self.lb_serial = QtWidgets.QLabel(sign_inDialog)
        self.lb_serial.setEnabled(True)
        self.lb_serial.setObjectName("lb_serial")
        self.gridLayout.addWidget(self.lb_serial, 0, 0, 1, 1)
        self.lb_id = QtWidgets.QLabel(sign_inDialog)
        self.lb_id.setObjectName("lb_id")
        self.gridLayout.addWidget(self.lb_id, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(sign_inDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 4, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 0, 1, 1, 1)
        self.cbx_laptop = QtWidgets.QCheckBox(sign_inDialog)
        self.cbx_laptop.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.cbx_laptop.setObjectName("cbx_laptop")
        self.gridLayout_2.addWidget(self.cbx_laptop, 2, 1, 1, 1)

        self.retranslateUi(sign_inDialog)
        self.buttonBox.accepted.connect(sign_inDialog.accept)
        self.buttonBox.rejected.connect(sign_inDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(sign_inDialog)

    def retranslateUi(self, sign_inDialog):
        _translate = QtCore.QCoreApplication.translate
        sign_inDialog.setWindowTitle(_translate("sign_inDialog", "Sign In Dialog"))
        self.lb_serial.setText(_translate("sign_inDialog", "Serial No."))
        self.lb_id.setText(_translate("sign_inDialog", "ID No."))
        self.cbx_laptop.setText(_translate("sign_inDialog", "No laptop?"))

