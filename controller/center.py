'''
Created on Mar 17, 2015

@author: michael
'''
from PyQt5 import QtWidgets

class Center():
    ''' The single role of this class is to center position
        for any window to be generated'''

    def __init__(self, window):

        # Get the geometry of the window including the window frame
        geometry = window.frameGeometry()
        # Get resolution of the screen and find its center
        resolution_center = QtWidgets.QDesktopWidget().availableGeometry().center()
        # Set the center of the window to the center of the screen
        geometry.moveCenter(resolution_center)
        window.move(geometry.topLeft())