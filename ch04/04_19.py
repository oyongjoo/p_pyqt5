import requests
import pandas as pd

url = "https://finance.naver.com/item/sise_day.nhn?code=066570"
resp = requests.get(url, headers={"user-agent": "Mozilla"})
df = pd.read_html(resp.text)
print(df[0].dropna())