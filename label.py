from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from Setting import Setting
from RevisePassword import RevisePassword

class Button(QPushButton):

    def __init__(self, parent=None):
        super(Button, self).__init__(parent)
        self.setAcceptDrops(True)
        self.name = None
        self.sex = None

    def setName(self, Name):
        self.name = Name

    def setSex(self, Sex):
        self.sex = Sex

    def contextMenuEvent(self, QContextMenuEvent):
        menu = QMenu(self)
        oneAction = menu.addAction('修改密码')
        twoAction = menu.addAction('修改头像和签名等')
        oneAction.triggered.connect(self.revisePassword)
        twoAction.triggered.connect(self.reviseOthers)
        menu.popup(self.mapToGlobal(QContextMenuEvent.pos()))

    def revisePassword(self):
        revise_Password = RevisePassword(self)
        revise_Password.mySignal.connect(self.getPasswordSignal)
        revise_Password.show()

    def reviseOthers(self):
        setting = Setting(self)
        setting.mySignal.connect(self.getSettingSignal)
        setting.show()

    def getPasswordSignal(self, message):
        print(message)

    def getSettingSignal(self, message):
        print(message)