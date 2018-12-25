import pymssql

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QToolBox, QListView, QMenu, QAction, QInputDialog, QMessageBox

from Ui_contacts import Ui_Dialog
from ListModel import ListModel
from ChatDialog import ChatDialog
from ListView import ListView
from addFriends import addFriends

class ContactsView(QToolBox,Ui_Dialog):
    def __init__(self, Name):
        super(ContactsView,self).__init__()
        self.setupUi(self)
        self.graphicsView_2.setStyleSheet("border-image: url(images/3.jpg);")
        self.label_2.setText("你的个性签名")
        self.pushButton_5.setToolTip('设置')
        self.pushButton_6.setToolTip('添加好友')
        self.listView.setStyleSheet("QListView{icon-size:70px}")
        self.Data_List = self.DataList_init(Name)
        self.pushButton_5.setName(self.label.text())
        self.name = Name
        self.sex, self.signature, self.iconpath = self.getIconAndSignatureSex()
        self.pushButton_5.setSex(self.sex)
        self.label_2.setText(self.signature)
        self.m_model = ListModel(self.Data_List)
        # print('hello')
        self.listView.setModel(self.m_model)
        
        # self.m_model.ListItemData
    
    def getIconAndSignatureSex(self):
        conn = pymssql.connect(server=r'LAPTOP-5N6O15EE\SQLEXPRESS',host='localhost:2301',database='Database',charset='utf8')
        cur = conn.cursor()
        cur.execute('select * from Persons where name=%s',self.name)
        tup = cur.fetchall()
        sex = tup[0][1]
        cur.execute('select * from PersonDetails where Name=%s',self.name)
        tup = cur.fetchall()
        signature = tup[0][1]
        iconpath = tup[0][2]
        cur.close()
        conn.close()
        return sex,signature,iconpath


    def DataList_init(self, Name):
        conn = pymssql.connect(server=r'LAPTOP-5N6O15EE\SQLEXPRESS',host='localhost:2301',database='Database',charset='utf8')
        cur = conn.cursor()
        cur.execute('select * from Friends where My=%s',Name)
        tup = cur.fetchall()
        message = []
        if len(tup)!=0:
            for item in tup:
                message.append(item[2])
        DataList = []
        for item in message:
            cur.execute('select * from PersonDetails where Name=%s',item)
            tup = cur.fetchall()
            # print(tup)
            dic = dict()
            dic['name'] = tup[0][0]
            dic['signature'] = tup[0][1]
            dic['iconPath'] = tup[0][2]
            DataList.append(dic)
        cur.close()
        conn.close()
        # print(DataList)
        return DataList

    def Chat(self,modelIndex):
        index = self.listView.currentIndex().row()
        message = self.m_model.getItem(index)
        message['登录头像'] = self.iconpath
        self.chatDialog = ChatDialog(message)
        self.chatDialog.show()

    # 添加联系人
    def AddContacts(self):
        addFriendsDialog = addFriends(self)
        addFriendsDialog.show()

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
