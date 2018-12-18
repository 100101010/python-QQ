from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QToolBox, QListView, QMenu, QAction, QInputDialog, QMessageBox

from Ui_contacts import Ui_Dialog
from ListModel import ListModel
from ChatDialog import ChatDialog
from ListView import ListView

class ContactsView(QToolBox,Ui_Dialog):
    def __init__(self):
        super(ContactsView,self).__init__()
        self.setupUi(self)
        self.graphicsView_2.setStyleSheet("border-image: url(images/3.jpg);")
        self.label_2.setText("你的个性签名")
        self.pushButton_5.setToolTip('设置')
        self.pushButton_6.setToolTip('添加好友')
        self.listView.setStyleSheet("QListView{icon-size:70px}")
    
    def Chat(self,modelIndex):
        index = self.listView.currentIndex().row()
        message = self.listView.m_pModel.getItem(index)
        self.chatDialog = ChatDialog(message)
        self.chatDialog.show()

    # 添加联系人
    def AddContacts(self):
        pass

    # 设置
    def SetSomething(self):
        pass

    # 展示信息
    def ShowMessage(self):
        pass

    # 展示联系人
    def ShowContacts(self):
        pass

    # 展示群
    def ShowGroup(self):
        pass

    # 展示搜索消息
    def ShowSearchMessage(self):
        pass
