# ch05/05_17.py
import pybithumb

df = pybithumb.get_ohlcv("BTC")
ma5 = df['close'].rolling(window=5).mean()
last_ma5 = ma5[-2]

print(ma5.tail(5))

price = pybithumb.get_current_price("BTC")

print(price, last_ma5)

if price > last_ma5:
    print("상승장")
else:
    print("하락장")