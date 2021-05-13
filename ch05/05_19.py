import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pybithumb

form_class = uic.loadUiType('..\\bull.ui')[0]

class MyWindow(QMainWindow, form_class):
    tickers = ['BTC', 'ETH', 'BCH', 'ETC']

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        timer = QTimer(self)
        timer.start(5000)
        timer.timeout.connect(self.timeout)

        self.tableWidget.setRowCount(len(self.tickers))

    def timeout(self):
        bull_list = ['상승장', '하락장']
        for i, ticker in enumerate(self.tickers):

            item = QTableWidgetItem(ticker)
            self.tableWidget.setItem(i, 0, item)
            price, ma5_last, state = self.get_market_infos(ticker)
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(price)))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(ma5_last)))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(state))

    def get_market_infos(self, ticker):
        df = pybithumb.get_ohlcv(ticker)
        ma5 = df['close'].rolling(window=5).mean()
        ma5_last = ma5[-2]
        price = pybithumb.get_current_price(ticker)
        if price > ma5_last:
            state = '상승장'
        else:
            state = '하락장'

        return price, ma5_last, state

app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()