# ch03/03_14.py
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 위젯 생성 코드
        rect = [100, 200, 300, 200]
        self.setGeometry(*rect)
        self.setWindowTitle("PyQt")
        self.setWindowIcon(QIcon('stock_01.png'))  # PyQt5.QtGui 필요

        btn = QPushButton("버튼1", self)
        btn.move(10, 10)
        btn.clicked.connect(self.btn_clicked)

        btn2 = QPushButton('버튼2', self)
        btn2.move(10, 40)

    # 이벤트 처리 코드
    @staticmethod
    def btn_clicked():
        print("버튼 클릭")

# QApplication 객체 생성 및 이벤트 루트 생성 코드
app = QApplication(sys.argv)  # 객체 생성
window = MyWindow()
window.show()
app.exec_()  # 이벤트 루프
