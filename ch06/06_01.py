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

# ch06/06_08.py
# 클래스 생성 생략
order = bithumb.sell_limit_order("BTC", 4000000, 1)
print(order)

# 이번에는 잔고를 조회해서 보유 중인 비트코인 수량만큼 지정가 매도 주문을 해보겠습니다.

# ch06/06_09.py
# 클래스 생성 코드 생략
unit = bithumb.get_balance("BTC")[0]
print(unit)
order = bithumb.sell_limit_order("BTC", 4000000, unit)
print(order)