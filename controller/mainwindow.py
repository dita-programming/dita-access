import datetime
from PyQt5 import QtCore, QtWidgets, QtGui
from view import Ui_MainWindow, StyledMessageBox, rc_dita
from controller import SignInDialog, Center, Startup
from model import Database, DAOFactory, ValidatorFactory, LogItem


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        Center(self)
        self.members_in_model = QtGui.QStandardItemModel(0, 1, self)
        self.members_in_model.setHeaderData(0, QtCore.Qt.Horizontal, "Members in")
        self.ui.treeView.setModel(self.members_in_model)
        self._db = Database()
        self.members_in = []
        self.sign_in = SignInDialog(self)
        self.sign_in.validation_finished.connect(self.sign_in_member)
        self.msg_box = StyledMessageBox(self)
        self.validator = None
        self.startup = Startup(self, self._db)
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
        self._db.start_connection()
        factory = DAOFactory(self._db)
        log_dao = factory.get_dao("log")
        log_dao.add_object(LogItem(mbr, self.get_time()))
        self.members_in.append(mbr)
        index = self.members_in.index(mbr)
        self.members_in_model.insertRow(index)
        self.members_in_model.setData(self.members_in_model.index(index, 0), mbr.name.split()[0].title())

    def sign_out_member(self, id_no):
        if not id_no:
            self.msg_box.show_message("Blank ID", "Please enter your student ID")
            return

        try:
            self._db.start_connection()
            factory = DAOFactory(self._db)
            member_dao = factory.get_dao("member")
            log_dao = factory.get_dao("log")
            member = member_dao.get_object(id_no)
            self.validator = ValidatorFactory(member_dao, None, log_dao, member, None).get_validator("sign out")

            if self.validator.validate():
                log_item = log_dao.get_incomplete_object(member.id)
                log_item.time_out = self.get_time()
                log_dao.update_object(log_item)
                mbr_in = next((mbr for mbr in self.members_in if mbr.get_details() == member.get_details()), None)
                index = self.members_in.index(mbr_in)
                self.members_in_model.removeRow(index)
                self.members_in.remove(mbr_in)
            else:
                raise Exception()
        except:
            pass
        finally:
            self.msg_box.show_message(self.validator.message[0], self.validator.message[1])
            self._db.close_connection()

    def load_session(self, members_list):
        if members_list:
            for member in members_list:
                name = member.name.split()[0].title()
                self.members_in.append(member)
                index = self.members_in.index(member)
                self.members_in_model.insertRow(index)
                self.members_in_model.setData(self.members_in_model.index(index, 0), name)

    def clean_up(self):
        """
        Cleans up current records on table change
        """
        self.members_in.clear()
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

    @staticmethod
    def get_time():
        """
        Returns current time
        """
        return datetime.datetime.now().time().replace(microsecond=0).strftime("%H:%M")
