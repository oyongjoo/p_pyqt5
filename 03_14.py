# ch03/03_14.py
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        rect = [100, 200, 300, 400]
        self.setGeometry(*rect)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
