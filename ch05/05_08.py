# ch05/05_08.py
import pybithumb

orderbook = pybithumb.get_orderbook("BTC")

asks = orderbook['asks']
bids = orderbook['bids']

print(bids)
print(asks)