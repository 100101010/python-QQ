import sys
import os

from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from Ui_chatset import Ui_Dialog

class chooseFile(QtWidgets.QMainWindow,Ui_Dialog):

    mySignal = pyqtSignal(dict)

    def __init__(self,parent = None):
        super(chooseFile,self).__init__(parent)
        self.setupUi(self)
        self.cwd = os.getcwd() # 获取当前程序文件位置
        self.lineEdit.setReadOnly(True)

    def OpenFiles(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,  
                                    "选取文件",  
                                    self.cwd, # 起始路径 
                                    "All Files (*)")   # 设置文件扩展名过滤,用双分号间隔
        self.lineEdit.setText(fileName_choose)

    def SetMessage(self):
        dic = {}
        dic['聊天背景'] = self.lineEdit.text()
        dic['字体'] = self.comboBox.currentText()
        dic['字体样式'] = self.comboBox_2.currentText()
        dic['字体大小'] = self.comboBox_3.currentText()
        self.mySignal.emit(dic)
        self.close()