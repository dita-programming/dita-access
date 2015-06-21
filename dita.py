#!/usr/bin/env python3
import sys
from PyQt5 import QtWidgets
from controller import MainWindow
                
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
    