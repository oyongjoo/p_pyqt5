# ch05/05_01.py
import pybithumb

tickers = pybithumb.get_tickers() # ticker 목록 얻기
print(tickers)