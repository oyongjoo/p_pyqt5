import time
import datetime

now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1) # 다음날 자정

while True:
    now = datetime.datetime.now()

    if mid < now < mid + datetime.timedelta(seconds=15): # 현재시간이 자정 + 10초 사이에 있는 경우는 자정이라고 판단.
        print("자정입니다.")
        now = datetime.datetime.now()
        mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)

    print(now, "vs", mid)
    time.sleep(1)