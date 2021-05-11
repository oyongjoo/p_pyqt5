# ch05/05_03.py
import pybithumb
import time

while True:
    price = pybithumb.get_current_price("BTC")
    print(price)
    time.sleep(1)
