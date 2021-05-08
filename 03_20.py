# ch03/03_20.py
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic  ## uic 모듈 사용하기

## uic 모듈의 loadUiType() 메서드는 Qt Designer의 결과물인 mywindow.ui 파일을 읽어서 파이썬 클래스 코드를 만듭니다.
form_class = uic.loadUiType("mywindow.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        # setupUi()는 form_class에 정의된 메서드로 Qt Designer에서 만든 클래스들을 초기화합니다.
        self.setupUi(self)

        self.pushButton.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        print("버튼 클릭")


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()