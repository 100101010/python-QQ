# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\web\UI_File\addFriends.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 566)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 111, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 10, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Gothic Std B")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(150, 10, 241, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(0, 50, 401, 521))
        self.listView.setObjectName("listView")

        self.retranslateUi(Dialog)
        self.lineEdit.editingFinished.connect(Dialog.search)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comboBox.setItemText(0, _translate("Dialog", "按姓名搜索"))
        self.comboBox.setItemText(1, _translate("Dialog", "按关键字搜索"))
        self.comboBox.setItemText(2, _translate("Dialog", "按性别搜索"))
        self.comboBox.setItemText(3, _translate("Dialog", "按地区搜索"))
        self.comboBox.setItemText(4, _translate("Dialog", "按身份证号搜索"))
        self.comboBox.setItemText(5, _translate("Dialog", "按电话号码搜索"))
        self.label.setText(_translate("Dialog", "："))

