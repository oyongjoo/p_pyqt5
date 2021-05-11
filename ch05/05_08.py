# ch05/05_08.py
import pybithumb

orderbook = pybithumb.get_orderbook("BTC")

asks = orderbook['asks']
bids = orderbook['bids']

# print(bids)
# print(asks)

for ask in asks:
    price = ask['price']
    quantity = ask['quantity']
    print(f"매도호가: {price}, 매도잔량: {quantity}")