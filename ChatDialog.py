from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from Ui_chat import Ui_Dialog
from ChatSet import chooseFile

class ChatDialog(QtWidgets.QMainWindow,Ui_Dialog):
    
    def __init__(self, Message):
        super(ChatDialog, self).__init__()
        self.setupUi(self)
        self.textEdit.setReadOnly(True)
        self.setDialogMessage(Message)
        self.time = datetime.now()

    def setDialogMessage(self, Message):
        self.setWindowTitle(Message['name'])
        self.setWindowIcon(QIcon(Message['iconPath']))

    def SendMessage(self):
        message = self.textEdit_2.toPlainText()
        self.textEdit.setAlignment(Qt.AlignRight)
        self.textEdit.append(message)
        self.textEdit_2.clear()

    def SendFile(self):
        pass
        
    def getFileName(self,dic):
        print(dic)

    def SendGraphics(self):
        pass

    def SetMessage(self):
        myFile = chooseFile(self)
        myFile.mySignal.connect(self.getFileName)
        myFile.show()

    def closeEvent(self, QCloseEvent):
        preSendMessage = self.textEdit_2.toPlainText()
        if len(preSendMessage) == 0:
            QCloseEvent.accept()
        else:
            res=QMessageBox.question(self,'消息','输入框存在待发送的消息,是否关闭？',QMessageBox.Yes|QMessageBox.No,QMessageBox.No) # 两个按钮是否， 默认No则关闭这个提示框
            if res==QMessageBox.Yes:
                QCloseEvent.accept()  
            else:
                QCloseEvent.ignore()