# Bithumb 클래스 객체 생성하기
import pybithumb
import time

con_key = "b592b4dc2d9edac280b80987fb3b17f8"
sec_key = "ecc4a67427a408e99d58f5fc3946d481"

bithumb = pybithumb.Bithumb(con_key, sec_key)

# 지정가로 주문하기, 현재로선 돈이 없어서 못산다.
order = bithumb.buy_limit_order("BTC", 57000000, 0.001)
print(order)

# 시장가로 주문하기
order = bithumb.buy_market_order("BTC", 1)