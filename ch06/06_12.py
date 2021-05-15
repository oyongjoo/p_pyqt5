import pybithumb
import time

# 주기적으로 현재가 얻어오기
while True:
    price = pybithumb.get_current_price("BTC")
    print(price)
    time.sleep(0.2)

