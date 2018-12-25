import sys
import pymssql

from PyQt5.QtWidgets import QLineEdit,QMessageBox,QCheckBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

from Ui_registerorlogon import Ui_MainWindow # 主窗口
from register import register
from Contacts import ContactsView

# 主窗口
# 实现登录检查功能
# 未实现记住密码和自动登录,输入智能提示
class mywindow(QtWidgets.QMainWindow,Ui_MainWindow):

    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.message = "账号或密码错误"
        self.message_2 = "请输入完整的账号和密码"
        self.form2 = register()
        # self.pushButton.setShortcutEnabled(True)
        self.pushButton.setShortcut(Qt.Key_Enter)
        self.lineEdit_2.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setPlaceholderText("密码6-15位，只能有数字和字母")
        self.graphicsView.setStyleSheet('border-image:url(images/2.jpg)')
        self.graphicsView_2.setStyleSheet('border-image:url(images/4.png)')
        self.setWindowIcon(QIcon('images/5.png'))
        conn = pymssql.connect(server=r'LAPTOP-5N6O15EE\SQLEXPRESS',host='localhost:2301',database='Database',charset='utf8')
        cur = conn.cursor()
        cur.execute('select * from Memory where First=%d',1)
        tup = cur.fetchall()
        if len(tup) != 0:
            self.lineEdit.setText(tup[0][0])
            # 如果已勾选记住密码
            if int(tup[0][2]) == 1:
                self.lineEdit_2.setText(tup[0][1])
                self.checkBox_2.setCheckState(Qt.Checked)
            # 如果已勾选自动登录
            if int(tup[0][3]) == 1:
                self.close()
                self.checkBox.setCheckState(Qt.Checked)
                self.Login()
        cur.close()
        conn.close()

    def sendName(self):
        name = self.lineEdit.text()
        self.mySignal.emit(name)

    # 实现自动登录和记住密码相联系
    def changeState(self):
        if self.checkBox.checkState():
            if not self.checkBox_2.checkState():
                self.checkBox_2.setCheckState(Qt.Checked)
    
    def changeState_2(self):
        if not self.checkBox_2.checkState():
            if self.checkBox.checkState():
                self.checkBox.setCheckState(Qt.Unchecked)

    def DeletePassword(self):
        self.lineEdit_2.setText('')

    def SearchPassword(self):
        account = self.lineEdit.text()
        if len(account) != 0:
            conn = pymssql.connect(server=r'LAPTOP-5N6O15EE\SQLEXPRESS',host='localhost:2301',database='Database',charset='utf8')
            cur = conn.cursor()
            cur.execute('select * from Memory where Account=%s',account)
            tup = cur.fetchall()
            cur.close()
            conn.close()
            if len(tup) != 0:
                if int(tup[0][2]) == 1:
                    self.lineEdit_2.setText(tup[0][1])
                    self.checkBox_2.setCheckState(Qt.Checked)
                if int(tup[0][3]) == 1:
                    self.close()
                    self.checkBox.setCheckState(Qt.Checked)
                    self.Login()
                    

    def newwindow(self):
        message_1 = self.lineEdit.text()
        message_2 = self.lineEdit_2.text()
        if len(message_1) == 0 or len(message_2) == 0:
            QMessageBox.warning(self,"警告",self.message_2)
        elif self.judge(message_1,message_2)==True:
            self.close()
            MemoryPassword = 0
            AutoLoginIn = 0
            # 如果勾选记住密码
            if self.checkBox_2.checkState():
                MemoryPassword = 1
                if self.checkBox.checkState():
                    AutoLoginIn = 1
            if MemoryPassword == 1 or AutoLoginIn == 1:
                conn = pymssql.connect(server=r'LAPTOP-5N6O15EE\SQLEXPRESS',host='localhost:2301',database='Database',charset='utf8')
                cur = conn.cursor()
                cur.execute('select * from Memory where Account=%s;select * from Memory where First=%d',(message_1,1))
                tup1 = cur.fetchall()
                cur.nextset()
                tup2 = cur.fetchall()
                if len(tup2) != 0:
                    cur.execute('update Memory set First=%d where Account=%s',(0,tup2[0][0]))
                if len(tup1) == 0:
                    cur.execute('insert into Memory values (%s,%s,%d,%d,%d)',(message_1,message_2,MemoryPassword,AutoLoginIn,1))
                else:
                    cur.execute('update Memory set Account=%s,Password=%s,RememberPassword=%d,AutoLoginIn=%d,First=%d where Account=%s',(message_1,message_2,MemoryPassword,AutoLoginIn,1,message_1))
                conn.commit()
                cur.close()
                conn.close()
            self.Login()
            
        else:
            QMessageBox.warning(self,"警告",self.message)
            # self.form1.show()

    def newregister(self):
        self.form2.show()
    
    def judge(self,name,password):
        conn = pymssql.connect(server=r'LAPTOP-5N6O15EE\SQLEXPRESS',host='localhost:2301',database='Database',charset='utf8')
        cur = conn.cursor()
        cur.execute('select * from Persons where name=%s',name)
        tup = cur.fetchall()
        cur.close()
        conn.close()
        if tup == None:
            return False
        else:
            for item in tup:
                if item[7] == password:
                    return True
            return False

    def Login(self):
        name = self.lineEdit.text()
        self.View = ContactsView(name)
        self.View.label.setText(name)
        self.View.show()