# ch03/03_14.py
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        rect = [100, 200, 300, 200]
        self.setGeometry(*rect)
        self.setWindowTitle("PyQt")
        self.setWindowIcon(QIcon('stock_01.png'))

        btn = QPushButton("버튼1", self)
        btn.move(10, 10)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
