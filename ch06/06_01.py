# Bithumb 클래스 객체 생성하기
import pybithumb
import time

con_key = "b592b4dc2d9edac280b80987fb3b17f8"
sec_key = "ecc4a67427a408e99d58f5fc3946d481"

bithumb = pybithumb.Bithumb(con_key, sec_key)
# balance = bithumb.get_balance('BTC')

for ticker in pybithumb.get_tickers():
    balance = bithumb.get_balance(ticker)
    print(ticker, ":", balance)
    time.sleep(0.1)