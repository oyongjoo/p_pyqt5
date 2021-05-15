import pybithumb

def get_target_price(ticker):
    df = pybithumb.get_ohlcv(ticker)
    print(df.tail())
    yesterday = df.iloc[-2]

    today_open = yesterday['close']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    target = today_open + (yesterday_high - yesterday_low) * 0.5
    return target



