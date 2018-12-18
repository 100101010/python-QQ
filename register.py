import pymssql
import re
import datetime
import time

from PyQt5.QtWidgets import QLineEdit,QMessageBox,QCheckBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt,QRegExp
from PyQt5.QtGui import QRegExpValidator

from Ui_register import Ui_Form1 # 注册窗口

# 注册窗口
# 可以检查是否已注册和一些常规的检查
# 包括身份证号和是否已注册，密码输入检查等
class register(QtWidgets.QMainWindow,Ui_Form1):
    def __init__(self):
        super(register,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("注册")
        self.message_1 = '信息未录入完全'
        self.message_2 = '两次输入密码的不相同'
        self.message_3 = '此账户已注册(系统检测到已有相同身份证号注册)'
        self.message_4 = '请先选择省，再选中市/区'
        self.message_5 = '注册成功'
        self.message_6 = '身份证号输入不合法'
        self.message_7 = '电话号码输入不合法'
        # 屏蔽密码框的右键菜单
        # 同时给出提示信息
        self.lineEdit_3.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_3.setEchoMode(QLineEdit.Password)
        self.lineEdit_3.setPlaceholderText("密码15位之内，只能有数字和字母")
        self.lineEdit_4.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_4.setEchoMode(QLineEdit.Password)
        self.lineEdit_4.setPlaceholderText("再次确认密码")
        self.lineEdit_4.setMaxLength(15) #设置最大长度
        #设置密码允许出现的字符内容为数字和字母
        reg=QRegExp('[a-zA-Z0-9]+$')
        #自定义文本验证器
        pValidator=QRegExpValidator(self)
        #设置属性
        pValidator.setRegExp(reg)
        self.lineEdit_3.setValidator(pValidator)

    def Add(self):
        conn = pymssql.connect(server=r'LAPTOP-5N6O15EE\SQLEXPRESS',host='localhost:2301',database='Database',charset='utf8')
        cur = conn.cursor()
        province = self.comboBox_3.currentText()
        cur.execute('select * from CityList where City=%s',province)
        tup = cur.fetchall()
        self.comboBox_4.clear()
        for i in tup[0]:
            if i!=None and i!=province:
                self.comboBox_4.addItem(i)
        cur.close()
        conn.close()

    def refresh(self):
        if self.comboBox_4.count()==0:
            QMessageBox.warning(self,"警告",self.message_4)
    
    def judgeIdNumber(self,idNumber,province):
        area = {"11": "北京", "12": "天津", "13": "河北", "14": "山西", "15": "内蒙古", "21": "辽宁", "22": "吉林", "23": "黑龙江", "31": "上海",
          "32": "江苏", "33": "浙江", "34": "安徽", "35": "福建", "36": "江西", "37": "山东", "41": "河南", "42": "湖北", "43": "湖南",
          "44": "广东", "45": "广西", "46": "海南", "50": "重庆", "51": "四川", "52": "贵州", "53": "云南", "54": "西藏", "61": "陕西",
          "62": "甘肃", "63": "青海", "64": "宁夏", "65": "新疆"}

        # 检验地区
        area_Id = idNumber[0:2]
        if area_Id not in area:
            return False
        if area[area_Id] != province[0:2]:
            return False
        
        # 检验闰年和平年
        def isPrimeYear(birthday):
            birthday_year = int(birthday[0:4])
            if birthday_year % 400 == 0:
                return True
            elif birthday_year % 4 == 0 and birthday_year % 100 != 0:
                return False
            else:
                return False
        
        # 如果身份证号为15位
        if len(idNumber) == 15:
            if isPrimeYear('19'+idNumber[6:8]):
                erg = re.compile(
                    '[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}$')  # //测试出生日期的合法性
            else:
                erg = re.compile(
                    '[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}$')  # //测试出生日期的合法性
            if (re.match(erg, idNumber)):
                return True
            else:
                return False
        # 如果身份证号是18位
        elif len(idNumber) == 18:
            if isPrimeYear(idNumber[6:10]):
                ereg = re.compile(
                    '[1-9][0-9]{5}(19[0-9]{2}|20[0-9]{2})((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}[0-9Xx]$')  # //闰年出生日期的合法性正则表达式
            else:
                ereg = re.compile(
                    '[1-9][0-9]{5}(19[0-9]{2}|20[0-9]{2})((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}[0-9Xx]$')  # //平年出生日期的合法性正则表达式
            # 测试出生日期的合法性

            # 这里首先检验输入的出生日期是否存在
            today = datetime.datetime.now()
            date = time.strptime(idNumber[6:14],'%Y%m%d')
            date1 = datetime.datetime(date[0],date[1],date[2])
            day1 = (today-date1).days
            if day1<0:
                return False
            
            if (re.match(ereg, idNumber)):
                # 计算校验位
                S = (int(idNumber[0]) + int(idNumber[10])) * 7 + (int(idNumber[1]) + int(idNumber[11])) * 9 + (int(
                    idNumber[2]) + int(idNumber[12])) * 10 + (int(idNumber[3]) + int(idNumber[13])) * 5 + (int(
                    idNumber[4]) + int(idNumber[14])) * 8 + (int(idNumber[5]) + int(idNumber[15])) * 4 + (int(
                    idNumber[6]) + int(idNumber[16])) * 2 + int(idNumber[7]) * 1 + int(idNumber[8]) * 6 + int(
                    idNumber[9]) * 3
                Y = S % 11
                M = 'F'
                JYM = '10X98765432'
                M = JYM[Y]  # 判断校验位
                if M == idNumber[17]:  # 检测ID的校验位
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


    def checkIdNumber(self,IdNumber):
        # 这里是链接数据库并检测录入的身份证号是否已经存在
        conn = pymssql.connect(server=r'LAPTOP-5N6O15EE\SQLEXPRESS',host='localhost:2301',database='Database',charset='utf8')
        cur = conn.cursor()
        str1 = self.lineEdit_5.text()
        cur.execute('select * from Persons where idNumber=%s',str1)
        tup = cur.fetchall()
        cur.close()
        conn.close()
        if len(tup)==0:
            return True
        else:
            return False
        

    def readmessage(self):
        name = self.lineEdit.text()  
        sex = self.comboBox.currentText()  
        nation = self.comboBox_2.currentText()  
        province = self.comboBox_3.currentText()  
        city = self.comboBox_4.currentText()  
        phoneNumber = self.lineEdit_2.text()  
        idNumber =  self.lineEdit_5.text()  
        password = self.lineEdit_3.text()  
        Qpassword = self.lineEdit_4.text()  
        if len(name)==0 or len(sex)==0 or len(nation)==0 or len(province)==0:
            QMessageBox.warning(self,"警告",self.message_1)
        elif len(city)==0 or len(phoneNumber)==0 or len(idNumber)==0:
            QMessageBox.warning(self,"警告",self.message_1)
        elif password!=Qpassword:
            QMessageBox.warning(self,"警告",self.message_2)
        elif self.checkIdNumber(idNumber)!=True:
            QMessageBox.warning(self,"警告",self.message_3)
        elif self.judgeIdNumber(idNumber,province)!=True:
            QMessageBox.warning(self,"警告",self.message_6)
        elif len(phoneNumber)!=11 or phoneNumber[0]!='1':
            QMessageBox.warning(self,'警告',self.message_7)
        elif len(password)<6:
            QMessageBox.warning(self,'警告',"密码长度太短")
        else:
            # 将注册信息写入数据库
            conn = pymssql.connect(server=r'LAPTOP-5N6O15EE\SQLEXPRESS',host='localhost:2301',database='Database',charset='utf8')
            cur = conn.cursor()
            cur.execute('insert into Persons values (%s,%s,%s,%s,%s,%s,%s,%s)',(name,sex,nation,province,city,phoneNumber,idNumber,password))
            conn.commit()
            cur.close()
            conn.close()
            # 提示注册成功
            QMessageBox.information(self,"温馨提示",self.message_5)
            # 关闭注册窗口
            self.close()