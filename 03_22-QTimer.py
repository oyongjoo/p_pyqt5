# QTimer 연습
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *  # QTimer 를 위해 import
import pykorbit


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.timer = QTimer(self)
        self.timer.start(1000)  # 1초 마다 반복
        self.timer.timeout.connect(self.timeout)  # 1초 마다 호출

    # 현재 시간 표시
    def timeout(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()