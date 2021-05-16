import time
import pybithumb
import datetime

def get_target_price(ticker='BTC'):
    df = pybithumb.get_ohlcv(ticker)
    yesterday = df.iloc[-2]

    today_open = yesterday['close']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    target = today_open + (yesterday_high - yesterday_low) * 0.5
    return target

now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1) # 다음날 자정
target_price = get_target_price("BTC")

while True:
    now = datetime.datetime.now()

    if mid < now < mid + datetime.timedelta(seconds=15): # 현재시간이 자정 + 10초 사이에 있는 경우는 자정이라고 판단.
        print("자정입니다.")
        target_price = get_target_price("BTC")
        mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)

    current_price = pybithumb.get_current_price("BTC")
    print(current_price)

    time.sleep(1)