from pandas import DataFrame
import os
data = {"open": [737, 750], "high": [755, 780], "low": [700, 710], "close": [750, 770]}
df = DataFrame(data, index=['2018-0101', '2018-0102'])
print(df)

import pandas as pd
df.to_excel("d:\\ohlc-2.xlsx")

df = pd.read_excel("D:\\Python\\p_pyqt5\\ohlc.xlsx", engine='openpyxl')
df = df.set_index('date')
print(df)