# ch05/05_08.py
import pybithumb

orderbook = pybithumb.get_orderbook("BTC")

asks = orderbook['asks']
bids = orderbook['bids']

# print(bids)
# print(asks)

for bid in bids:
    price = bid['price']
    quantity = bid['quantity']
    print(f"매수호가: {price}, 매수잔량: {quantity}")