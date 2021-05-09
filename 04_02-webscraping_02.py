# 종목 코드 입력시 해당 종목의 per, dvr 를 얻는 function
import requests
from bs4 import BeautifulSoup

def get_per(code):
    url = "https://finance.naver.com/item/main.nhn?code=" + code
    html = requests.get(url).text

    soup = BeautifulSoup(html, "html5lib")
    tags = soup.select("#_per")
    tag = tags[0]
    return float(tag.text)

def get_dividend(code):
    url = "https://finance.naver.com/item/main.nhn?code=" + code
    html = requests.get(url).text

    soup = BeautifulSoup(html, "html5lib")
    tag = soup.select("#_dvr")[0]
    return float(tag.text)

# 000660 - SK하이닉스
print(get_per("000660"))
print(get_dividend("000660"))