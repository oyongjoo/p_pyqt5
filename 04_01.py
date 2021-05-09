import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.nhn?code=000660"
# url ="https://finance.naver.com/sise/sise_market_sum.nhn?page=1"
html = requests.get(url).text

soup = BeautifulSoup(html, 'html5lib')
# tags = soup.select("#_per")
tags = soup.select("#_dvr")
# tags2 = soup.select("#_market_sum")
tag = tags[0]
print(tag.text)
# market_sum = tags2[0]
# print(market_sum.text.split())

# stock_head = soup.find("thead").find_all("th")
# data_head = [head.get_text() for head in stock_head]
#
# print(data_head)