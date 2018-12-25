#coding=utf-8

from PyQt5.QtWidgets import QListView, QMenu, QAction, QMessageBox
from PyQt5.QtCore import QSize
from ListModel import ListModel

class ListView(QListView):
    def __init__(self,parent = None):
        super(ListView,self).__init__(parent)
        self.map_listview = []
        # self.m_pModel = ListModel()  
        # self.setModel(self.m_pModel)

    def contextMenuEvent(self, event):
        hitIndex = self.indexAt(event.pos()).column()
        if hitIndex > -1:
            pmenu = QMenu(self)
            pDeleteAct = QAction("删除好友",pmenu)
            pmenu.addAction(pDeleteAct)
            pDeleteAct.triggered.connect(self.deleteItemSlot)
            pmenu.popup(self.mapToGlobal(event.pos()))
    
    def deleteItemSlot(self):
        index = self.currentIndex().row()
        if index > -1:
            self.m_pModel.deleteItem(index)

    def setListMap(self, listview):
        self.map_listview.append(listview)

    def addItem(self, pitem):
        self.m_pModel.addItem(pitem)