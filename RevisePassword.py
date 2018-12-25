from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from Ui_revisePassword import Ui_Dialog

class RevisePassword(QtWidgets.QMainWindow, Ui_Dialog):

    mySignal = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        font = QtGui.QFont()
        font.setFamily("Adobe Gothic Std B")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit_2.setFont(font)
        self.lineEdit_3.setFont(font)

    def reviseMyPassword(self):
        if self.lineEdit_2.text() == self.lineEdit_3.text():
            self.mySignal.emit(self.lineEdit_2.text())
            self.close()
        else:
            QMessageBox.warning(self,'警告','两次输入密码不同')