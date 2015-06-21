# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Mon Jun 22 00:34:20 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(627, 562)
        MainWindow.setMinimumSize(QtCore.QSize(150, 100))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/DITA LOGO.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
"    background:white;\n"
"}\n"
"QTreeView {\n"
"    border-radius:6px;\n"
"    border:1px solid #29668f;\n"
"    font-weight:bold;\n"
"}\n"
"QFrame {    \n"
"    border-radius:6px;\n"
"    margin: 10px;\n"
"    background: white;\n"
"    /*border: 1px solid black;*/\n"
"    opacity: 0.5;\n"
"}\n"
"\n"
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
"    background:#ffffff;\n"
"    border-radius:6px;\n"
"    border:1px solid #29668f;\n"
"    font-weight:bold;\n"
"    padding:6px 24px;\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(300, 300))
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/DITA LOGO.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridFrame = QtWidgets.QFrame(self.centralwidget)
        self.gridFrame.setStyleSheet("QFrame {    \n"
"    margin: 10px;\n"
"    background: white;\n"
"    border: 1px solid black;\n"
"    opacity: 0.5;\n"
"}\n"
"\n"
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
"    background:#ffffff;\n"
"    border-radius:6px;\n"
"    border:1px solid #29668f;\n"
"    font-weight:bold;\n"
"    padding:6px 24px;\n"
"}\n"
"\n"
"\n"
"")
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.idLineEdit = QtWidgets.QLineEdit(self.gridFrame)
        self.idLineEdit.setObjectName("idLineEdit")
        self.horizontalLayout_2.addWidget(self.idLineEdit)
        self.signoutButton = QtWidgets.QPushButton(self.gridFrame)
        self.signoutButton.setObjectName("signoutButton")
        self.horizontalLayout_2.addWidget(self.signoutButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.laptopButton = QtWidgets.QPushButton(self.gridFrame)
        self.laptopButton.setStyleSheet("")
        self.laptopButton.setObjectName("laptopButton")
        self.gridLayout.addWidget(self.laptopButton, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.gridFrame)
        spacerItem2 = QtWidgets.QSpacerItem(20, 95, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeView.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.treeView.setObjectName("treeView")
        self.verticalLayout.addWidget(self.treeView)
        self.adminButton = QtWidgets.QPushButton(self.centralwidget)
        self.adminButton.setObjectName("adminButton")
        self.verticalLayout.addWidget(self.adminButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dita Access"))
        self.idLineEdit.setPlaceholderText(_translate("MainWindow", "ID"))
        self.signoutButton.setText(_translate("MainWindow", "Signout"))
        self.laptopButton.setText(_translate("MainWindow", "Signin"))
        self.adminButton.setText(_translate("MainWindow", "Admin"))
