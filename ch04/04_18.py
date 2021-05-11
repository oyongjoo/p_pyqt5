import pandas as pd
import urllib3

url = "https://finance.naver.com/item/sise_day.nhn?code=066570"
header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko)'}
http = urllib3.PoolManager()
req = http.request('GET', url, headers=header)

table = pd.read_html(req.data)
df = table[0].dropna(axis=0)
print(df)