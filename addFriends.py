from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from Ui_addFriends import Ui_Dialog

class addFriends(QtWidgets.QMainWindow,Ui_Dialog):

    def __init__(self, parent=None):
        super(addFriends, self).__init__(parent)
        self.setupUi(self)

    def search(self):
        searchMessage = self.lineEdit.text()
        # 未完成