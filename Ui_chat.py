# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\web\chat.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets,QtWebEngineWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
# from PyQt5.QtWebEngineWidgets import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(852, 531)
        # self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit = QtWebEngineWidgets.QWebEngineView(Dialog)
        url = 'file:///F:/vs%20code%E5%B7%B2%E5%AE%8C%E6%88%90%E9%A1%B9%E7%9B%AE/HTML5/a.html'
        # 指定打开界面的 URL
        self.textEdit.setUrl(QUrl(url))
        # 添加浏览器到窗口中
        # self.setCentralWidget(self.browser)
        self.textEdit.setContextMenuPolicy(Qt.NoContextMenu)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 851, 311))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 340, 851, 121))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(550, 480, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(700, 480, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 310, 31, 28))
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/11.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 310, 31, 28))
        self.pushButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/12.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 310, 31, 28))
        self.pushButton_5.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/13.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon2)
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.SendMessage)
        self.pushButton_2.clicked.connect(Dialog.close)
        self.pushButton_3.clicked.connect(Dialog.SendFile)
        self.pushButton_4.clicked.connect(Dialog.SendGraphics)
        self.pushButton_5.clicked.connect(Dialog.SetMessage)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "发送"))
        self.pushButton_2.setText(_translate("Dialog", "关闭"))
        self.pushButton_3.setToolTip(_translate("Dialog", "发送文件"))
        self.pushButton_4.setToolTip(_translate("Dialog", "发送图片"))
        self.pushButton_5.setToolTip(_translate("Dialog", "设置字体"))

