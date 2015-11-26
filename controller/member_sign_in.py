from PyQt5 import QtWidgets, QtCore

from view import Ui_sign_inDialog, StyledMessageBox
from model import Database, MemberDO, DAOFactory, ValidatorFactory


class SignInDialog(QtWidgets.QDialog):
    validation_finished = QtCore.pyqtSignal(MemberDO)

    def __init__(self, parent):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = Ui_sign_inDialog()
        self.ui.setupUi(self)
        self.model = self.parent().members_in_model
        self.msg_box = StyledMessageBox(None)
        self.db = Database()

    @QtCore.pyqtSlot()
    def on_cbx_laptop_clicked(self):
        if not self.ui.cbx_laptop.isChecked():
            self.ui.lb_serial.setEnabled(True)
            self.ui.txt_serial.setEnabled(True)
        else:
            self.ui.lb_serial.setEnabled(False)
            self.ui.txt_serial.setEnabled(False)
    
    def reset(self):
        """
        Reset the dialog box for new input
        """
        self.ui.txt_id.clear()
        self.ui.txt_serial.clear()
        self.ui.txt_serial.setEnabled(True)
        self.ui.lb_serial.setEnabled(True)
        self.ui.cbx_laptop.setChecked(False)
        
    def accept(self):
        success = True
        id_no = self.ui.txt_id.text()
        serial_no = self.ui.txt_serial.text().lower()

        if not serial_no and not self.ui.cbx_laptop.isChecked():
            self.msg_box.show_message("Blank Serial", "Please enter your laptops' serial No.")
            return
        
        if not id_no:
            self.msg_box.show_message("Blank ID", "Please enter your student ID")
            return

        try:
            db = Database()
            db.start_connection()
            factory = DAOFactory(db)
            member_dao = factory.get_dao("member")
            laptop_dao = factory.get_dao("laptop")
            log_dao = factory.get_dao("log")
            member = member_dao.get_object(id_no)
            laptop = laptop_dao.get_object(serial_no)
            validator = ValidatorFactory(member_dao, laptop_dao, log_dao, member, laptop).get_validator("sign in")
            validator.no_laptop_checked = self.ui.cbx_laptop.isChecked()
            if validator.validate():
                self.validation_finished.emit(member)
            else:
                raise Exception()
        except Exception:
            success = False
        finally:
            self.msg_box.show_message(validator.message[0], validator.message[1])
            db.close_connection()
            if success:
                return QtWidgets.QDialog.accept(self)
            else:
                return