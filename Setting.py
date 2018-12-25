import os
import sys

from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from Ui_setting import Ui_Dialog

class Setting(QtWidgets.QMainWindow, Ui_Dialog):

    mySignal = pyqtSignal(dict)

    def __init__(self, parent=None):
        super(Setting,self).__init__(parent)
        self.setupUi(self)
        self.lineEdit.setReadOnly(True)
        self.cwd = os.getcwd()

    def openFileDialog(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,  
                                    "选取文件",  
                                    self.cwd, # 起始路径 
                                    "JPG Files (*.jpg);;PNG Files (*.png)")   # 设置文件扩展名过滤,用双分号间隔
        self.lineEdit.setText(fileName_choose)

    def reviseOtherMessage(self):
        dic = dict()
        Icon = self.lineEdit.text()
        if len(Icon)!=0:
            dic['头像'] = Icon
        else:
            dic['头像'] = None
        if len(self.lineEdit_2.text())!=0:
            dic['签名'] = self.lineEdit_2.text()
        else:
            dic['签名'] = None
        dic['性别'] = self.comboBox.currentText()
        dic['电话号码'] = self.lineEdit_3.text()
        self.mySignal.emit(dic)
        self.close()