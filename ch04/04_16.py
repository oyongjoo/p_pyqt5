from pandas import DataFrame
data = {"open": [737, 750], "high": [755, 780], "low": [700, 710], "close": [750, 770]}
df = DataFrame(data, index=['2018-0101', '2018-0102'])
print(df)