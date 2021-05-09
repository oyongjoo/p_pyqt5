import requests

r = requests.get("https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw")
bitconin = r.json()
print(bitconin)
print(type(bitconin))