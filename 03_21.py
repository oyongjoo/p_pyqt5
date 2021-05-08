# 비트 코인 시세 조회 window
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import pykorbit

form_class = uic.loadUiType("window.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.inquiry)

    # BTC의 현재 가격을 얻어오는 function
    def inquiry(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time)
        price = pykorbit.get_current_price("BTC")
        self.lineEdit.setText(str(price))

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()