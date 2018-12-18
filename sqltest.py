# -*- utf-8 -*-
# import pymssql

# conn = pymssql.connect(server=r'LAPTOP-5N6O15EE\SQLEXPRESS',host='localhost:2301',database='Database',charset='utf8')
# cur = conn.cursor()
# str1 = '重庆'
# cur.execute('select * from CityList where City=%s',str1)
# tup = cur.fetchall()
# print(type(tup[0]))
# cur.close()
# conn.close()
# import re

# erag = re.compile(r'[1-2][0-9]{3}')
# year = '1999'+'165'
# print(year)
# print(re.match(erag,year))
# import datetime
# import time

# today = datetime.datetime.now()
# date = time.strptime('20190122','%Y%m%d')
# date1 = datetime.datetime(date[0],date[1],date[2])
# day1 = (today-date1).days
# print(day1)
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.myButton = QtWidgets.QPushButton(self)
        self.myButton.setObjectName("myButton")
        self.myButton.setText("Test")
        self.myButton.clicked.connect(self.msg)

    def msg(self):
        directory1 = QFileDialog.getExistingDirectory(self,
                                    "选取文件夹",
                                    "./")                                 #起始路径
        print(directory1)

        fileName1, filetype = QFileDialog.getOpenFileName(self,
                                    "选取文件",
                                    "./",
                                    "All Files (*);;Text Files (*.txt)")   #设置文件扩展名过滤,注意用双分号间隔
        print(fileName1,filetype)

        files, ok1 = QFileDialog.getOpenFileNames(self,
                                    "多文件选择",
                                    "./",
                                    "All Files (*);;Text Files (*.txt)")
        print(files,ok1)

        fileName2, ok2 = QFileDialog.getSaveFileName(self,
                                    "文件保存",
                                    "./",
                                    "All Files (*);;Text Files (*.txt)")

if __name__=="__main__":  
    import sys  
  
    app=QtWidgets.QApplication(sys.argv)  
    myshow=MyWindow()
    myshow.show()
    sys.exit(app.exec_())  