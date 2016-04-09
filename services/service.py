import datetime
import time
from PyQt5 import QtCore


class BackgroundService(QtCore.QObject):
    clean_up = QtCore.pyqtSignal()
    finished = QtCore.pyqtSignal()
    current_date = datetime.datetime.now().date()

    def __init__(self):
        super(BackgroundService, self).__init__()

    def reset(self):
        if self.current_date != datetime.datetime.now().date():
            self.current_date = datetime.datetime.now().date()
            self.clean_up.emit()

        time.sleep(3600)
        self.reset()
