import pybithumb
from talib.abstract import _ta_lib as ta
from talib import MA_Type
import numpy as np


arrClose = np.array(pybithumb.get_ohlcv('BTC')['close'])
macd, macd_signal, macdhist = ta.MACD(arrClose, 12, 26, 9)
