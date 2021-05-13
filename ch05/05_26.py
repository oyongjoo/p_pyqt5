import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import pybithumb
import time

tickers = ['BTC', 'ETH', 'BCH', 'ETC']
form_class = uic.loadUiType("../bull.ui")[0]

class Worker(QThread):
    def run(self):
        while True:
            data = {}

            for ticker in tickers:
                data[ticker] = self.get_market_infos(ticker)

            print(data)
            time.sleep(5)

    def get_market_infos(self, ticker):
        try:
            df = pybithumb.get_ohlcv(ticker)
            ma5 = df['close'].rolling(window=5).mean()
            ma5_last = ma5[-2]

            price = pybithumb.get_current_price(ticker)
            if price > ma5_last:
                status = "상승장"
            else:
                status = "하락장"

            return price, ma5_last, status
        except:
            return None, None, None

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.worker = Worker()
        self.worker.start()

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
