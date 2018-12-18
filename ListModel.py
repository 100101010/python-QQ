#coding=utf-8

from PyQt5.QtCore import QAbstractListModel, Qt, QModelIndex, QVariant, QSize
from PyQt5.QtGui import QIcon, QFont
import Random_Name, random

class ListModel(QAbstractListModel):
    def __init__(self):
        super().__init__()     
        self.ListItemData = []
        self.Data_init()
       
    def data(self, index, role):
        if index.isValid() or (0 <= index.row() < len(self.ListItemData)):
            if role == Qt.DisplayRole:
                return QVariant(self.ListItemData[index.row()]['name']+'\n'+self.ListItemData[index.row()]['signature'])
            elif role == Qt.DecorationRole:
                return QVariant(QIcon(self.ListItemData[index.row()]['iconPath']))
            elif role == Qt.SizeHintRole:
                return QVariant(QSize(70,80))
            elif role == Qt.TextAlignmentRole:
                return QVariant(int(Qt.AlignLeft|Qt.AlignVCenter))
            elif role == Qt.FontRole:
                font = QFont()
                font.setPixelSize(20)
                return QVariant(font)
        else:            
            return QVariant()

    def rowCount(self, parent = QModelIndex()):
        return len(self.ListItemData)

    def Data_init(self):
        for i in range(1, 8):
            randname = Random_Name.getname()
            ItemData = {'name':'', 'iconPath':'', 'signature':''}
            ItemData['name'] = randname
            ItemData['iconPath'] = "./res/"+ str(i) + ".jpg"
            ItemData['signature'] = '暂无个性签名'
            self.addItem(ItemData)
            # self.ListItemData.append(ItemData)

    def addItem(self, itemData):
        if itemData: 
            self.beginInsertRows(QModelIndex(), len(self.ListItemData), len(self.ListItemData) + 1)
            self.ListItemData.append(itemData)
            self.endInsertRows()

    def deleteItem(self, index):
        del self.ListItemData[index]

    def getItem(self, index):
        if index > -1 and index < len(self.ListItemData):
            return self.ListItemData[index]
