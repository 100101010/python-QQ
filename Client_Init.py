import sys

from PyQt5 import QtWidgets

from Login import mywindow  # 导入主窗口

app = QtWidgets.QApplication(sys.argv)
window = mywindow()
window.show()
sys.exit(app.exec_())