# ch05/05_14.py
import pybithumb
from talib.abstract import _ta_lib as ta

btc = pybithumb.get_ohlcv("BTC")
close = btc['close']

ma5 = close.rolling(window=5).mean()

# ma5 = ta.SMA(close, timeperiod=5)
print(ma5.head(20))