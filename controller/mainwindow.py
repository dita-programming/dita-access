import datetime
from PyQt5 import QtCore, QtWidgets, QtGui

from model.do import Member, Log
from view import Ui_MainWindow, StyledMessageBox, rc_dita
from controller import SignInDialog, Center, Startup
from model import ValidatorFactory


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        Center(self)
        self.members_in_model = QtGui.QStandardItemModel(0, 1, self)
        self.members_in_model.setHeaderData(0, QtCore.Qt.Horizontal, "Members in")
        self.ui.treeView.setModel(self.members_in_model)
        self.members_in = []
        self.sign_in = SignInDialog(self)
        self.sign_in.validation_finished.connect(self.sign_in_member)
        self.msg_box = StyledMessageBox(self)
        self.validator = None
        self.startup = Startup(self)
        self.startup.prev_session_loaded.connect(self.load_session)
        self.startup.start_thread()
        QtCore.QTimer.singleShot(200, self.startup.load_previous_session)

    def closeEvent(self, event):
        """
        Intercept the close event in order to to destroy the
        background thread
        """
        # self.startup.thread.quit()
        return QtWidgets.QMainWindow.closeEvent(self, event)

    @QtCore.pyqtSlot()
    def on_laptopButton_clicked(self):
        '''
        Slot to process laptopButton click
        '''
        self.sign_in.reset()
        self.sign_in.show()

    @QtCore.pyqtSlot()
    def on_idLineEdit_returnPressed(self):
        id_no = self.ui.idLineEdit.text()
        self.sign_out_member(id_no)

    @QtCore.pyqtSlot()
    def on_signoutButton_clicked(self):
        '''
        Slot to process signoutButton click
        '''
        id_no = self.ui.idLineEdit.text()
        self.sign_out_member(id_no)

    @QtCore.pyqtSlot()
    def on_adminButton_clicked(self):
        '''
        Slot to process adminButton click
        '''
        pass

    def sign_in_member(self, mbr):
        log = Log(member=mbr)
        log.save()
        self.members_in.append(mbr)
        index = self.members_in.index(mbr)
        self.members_in_model.insertRow(index)
        self.members_in_model.setData(self.members_in_model.index(index, 0), self.format_disaply(mbr))

    def sign_out_member(self, id_no):
        if not id_no:
            self.msg_box.show_message("Blank ID", "Please enter your student ID")
            return

        try:

            member = Member.objects(id_no=id_no).first()
            self.validator = ValidatorFactory(member, None).get_validator("sign out")

            if self.validator.validate():
                log = Log.objects(member=member, time_out=None).first()
                log.time_out = self.get_time()
                log.save()
                mbr_in = next((mbr for mbr in self.members_in if mbr == member), None)
                index = self.members_in.index(mbr_in)
                self.members_in_model.removeRow(index)
                self.members_in.remove(mbr_in)
            else:
                raise Exception()
        except:
            pass
        finally:
            self.msg_box.show_message(self.validator.message[0], self.validator.message[1])
            self.ui.idLineEdit.clear()

    def load_session(self, members_list):
        if members_list:
            for member in members_list:
                self.members_in.append(member)
                index = self.members_in.index(member)
                self.members_in_model.insertRow(index)
                self.members_in_model.setData(self.members_in_model.index(index, 0), self.format_display(member))

    def clean_up(self):
        """
        Cleans up current records on table change
        """
        self.members_in.clear()
        self.members_in_model.removeRows(0, self.members_in_model.rowCount())


    @staticmethod
    def get_time():
        """
        Returns current time
        """
        return datetime.datetime.now().time().replace(microsecond=0).strftime("%H:%M")

    @staticmethod
    def format_display(mbr):
        return '[{}] {}'.format(mbr.major, mbr.name.split()[0].title())
