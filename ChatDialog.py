from datetime import datetime
import os

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
        # self.textEdit.setReadOnly(True)
        # font = QtGui.QFont()
        # font.setFamily("Adobe Gothic Std B")
        # font.setPointSize(12)
        # font.setBold(True)
        # font.setWeight(75)
        # self.textEdit.setFont(font)
        # self.textEdit.setLineWrapMode(QTextEdit.NoWrap)
        # self.textEdit.setAlignment(Qt.AlignRight)
        self.Icon = Message['登录头像']
        self.setDialogMessage(Message)
        self.pushButton.setShortcut(Qt.Key_Enter)
        self.time = datetime.now()
        self.cwd = os.getcwd() # 获取当前程序文件位置

    def setDialogMessage(self, Message):
        self.setWindowTitle(Message['name'])
        self.setWindowIcon(QIcon(Message['iconPath']))

    def SendMessage(self):
        message = self.textEdit_2.toPlainText()
        if len(message) == 0:
            QMessageBox.warning(self,'警告','发送消息不能为空')
        else:
            with open('F:\\vs code已完成项目\\HTML5\\c.html','w',encoding='utf-8') as f1:
                with open('F:\\vs code已完成项目\\HTML5\\a.html','r',encoding='utf-8') as f:
                    data = f.readlines()
                    pattern = '''<div class="receiver">
        <div>
            <img src="{0}">
        </div>
    <div>
        <div class="right_triangle"></div>
        <span>{1}</span>
    </div>
    </div>
</body>
'''
                    # print(data)
                    index = data.index('</body>\n')
                    html = pattern.format(self.Icon,message)
                    # print(index)
                    data[index] = html
                    data = ''.join(data)
                f1.write(data)

            with open('F:\\vs code已完成项目\\HTML5\\a.html','w',encoding='utf-8') as f1:
                with open('F:\\vs code已完成项目\\HTML5\\c.html','r',encoding='utf-8') as f2:
                    data = f2.readlines()
                f1.writelines(data)
            self.textEdit.reload()
            # self.textEdit.setAlignment(Qt.AlignRight)
            # self.textEdit.append(message)
            self.textEdit_2.clear()

    def SendFile(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,  
                                    "选取文件",  
                                    self.cwd, # 起始路径 
                                    "All Files (*)")   # 设置文件扩展名过滤,用双分号间隔
        self.textEdit_2.setText(fileName_choose)
        
    def getFileName(self,dic):
        pass
        # self.textEdit.setStyleSheet('border-image:url({0});'.format(dic['聊天背景']))

    def SendGraphics(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,  
                                    "选取文件",  
                                    self.cwd, # 起始路径 
                                    "JPG Files (*.jpg);;PNG Files (*.png)")   # 设置文件扩展名过滤,用双分号间隔
        with open('F:\\vs code已完成项目\\HTML5\\c.html','w',encoding='utf-8') as f1:
            with open('F:\\vs code已完成项目\\HTML5\\a.html','r',encoding='utf-8') as f:
                data = f.readlines()
                pattern = '''<div class="receiver">
        <div>
            <img src="{0}">
        </div>
    <div>
        <div class="right_triangle"></div>
            <img src="{1}" height="200">
    </div>
    </div>
</body>
'''
                # print(data)
                index = data.index('</body>\n')
                html = pattern.format(self.Icon,fileName_choose)
                data[index] = html
                data = ''.join(data)
            f1.write(data)

        with open('F:\\vs code已完成项目\\HTML5\\a.html','w',encoding='utf-8') as f1:
            with open('F:\\vs code已完成项目\\HTML5\\c.html','r',encoding='utf-8') as f2:
                data = f2.readlines()
            f1.writelines(data)
        self.textEdit.reload()
        # self.textEdit.setAlignment(Qt.AlignRight)
        # self.textEdit.append('<img src={0} height="200"></img>'.format(fileName_choose))

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