import pandas as pd
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

import talib
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
from matplotlib.pylab import date2num
import mplfinance as fplt
import FinanceDataReader as fdr
from matplotlib import font_manager, rc
import plotly.graph_objects as go
import chart_studio.plotly as py
import chart_studio
import cufflinks as cf

chart_studio.tools.set_credentials_file(username='oyongjoo', api_key='yZiEMstZd7qtusjo3RMW')

from chart_studio.plotly import plot, iplot
cf.go_offline(connected=True)

# Get today's date as UTC timestamp
today = datetime.today().strftime("%d/%m/%Y")
today = datetime.strptime(today + " +0000", "%d/%m/%Y %z")
to = int(today.timestamp())
# Get date ten years ago as UTC timestamp
ten_yr_ago = today-relativedelta(years=10)
fro = int(ten_yr_ago.timestamp())

# 한글 폰트 지정
# font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
# rc('font', family=font_name)
#
# from pandas_datareader import data
# from datetime import datetime
# import pandas as pd
#
# # 데이터를 가져올 날짜 설정
# start_date = datetime(2013,1,3)
# end_date = datetime(2021,1,22)
#
# # 야후에서 삼성전자 데이터 가져오기
# samsung = data.get_data_yahoo("005930.ks", start_date, end_date)
# samsung.reset_index(inplace=True)
#
# print(samsung.head())
#
# fig = go.Figure()
#
#
#
# # QuantFig 매소드를 사용해서 그래프 그리기
# qf=cf.QuantFig(samsung,title='Samsung Quant Figure',legend='top',name='삼성')
# qf.iplot()

quarterly = [

 '2019-01-23',  # 작년 4분기는 다음해 1월 말 ~ 2월 초 사이에
 '2019-02-08',
 '2019-04-22',  # 그해 1분기는 끝난 다음달(4월) 말 ~ 다다음달(5월) 초 사이에
 '2019-05-10',
 '2019-07-23',  # 마찬가지로 비슷
 '2019-08-09',
 '2019-10-23',
 '2019-11-08',
 '2020-01-23',
 '2020-02-10',
 '2020-04-22',
 '2020-05-08',
 '2020-07-21',  # 아직 2020년 2분기 발표가 다가오지 않은 시점이기 때문에 예외처리를 위해 데이터 삽입
 '2020-07-22'
]

shape_list = []  # 실적발표 기간을 나타내는 하이라이팅을 담당해 줄 dict 데이터를 리스트 변수에 담는다.
for num in range(0,len(quarterly), 2):
    shape_list.append(dict(
            type="rect",
            xref="x",
            yref="paper",
            x0=quarterly[num],
            y0=0,
            x1=quarterly[num+1],
            y1=1,
            fillcolor="LightSalmon",
            opacity=0.3,
            layer="below",
            line_width=0,
        ))


# 코로나 구간 추가
shape_list.append(dict(
            type="rect",
            xref="x",
            yref="paper",
            x0="2020-02-25",
            y0=0,
            x1="2020-04-20",
            y1=1,
            fillcolor="LightSeaGreen",
            opacity=0.3,
            layer="below",
            line_width=0)
                 )

company = "삼성전자"

df = fdr.DataReader('005930', '2019-01-02')
df = df.reset_index()
print(df.head())

from plotly.subplots import make_subplots

# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# candlestick = go.Candlestick(
#                             x=df.index,
#                             open=df['Open'],
#                             high=df['High'],
#                             low=df['Low'],
#                             close=df['Close']
#                             )
#
#
# fig = go.Figure(data=[candlestick])

fig.add_trace(go.Candlestick(
              x=df['Date'],
              open=df['Open'],
              high=df['High'],
              low=df['Low'],
              close=df['Close']
              ),
            secondary_y=True)

# include a go.Bar trace for volumes
fig.add_trace(go.Bar(x=df['Date'], y=df['Volume']),
               secondary_y=False)

fig.layout.yaxis2.showgrid=False

# 주식 데이터 쫙 깔고
# fig.add_trace(go.Scatter(x=df['Date'],
#                          y=df['Close'],
#                          mode='lines+markers',
#                          marker=dict(size=1)))


# 실적 발표 기간 하이라이팅
# fig.update_layout(title=f'{company}의 실적 발표 시즌 주가 변동',
#                   shapes=shape_list)
#
#
# # 코로나 주석 텍스트 추가
# fig.add_trace(go.Scatter(x=["2020-03-15"],
#                          y=[100000],
#                          text = "코로나 영향 주가 하향 기간",
#                          mode="text"))
#
#
# # html 익스포팅 코드 - 나만 보려면 안 써도 됩니다.
#
# plot(fig, filename = f'{company} 실적 발표 무렵 주가', auto_open=True)

fig.update_layout(xaxis_rangeslider_visible=False)
fig.show()


#
# qf = cf.QuantFig(df, title="삼성전자", legend='top', name='삼성')
# qf.iplot()
#
# layout = {
#     'font': {
#         'family': font_name,
#         'size': 20,
#         'color': 'blue'
#     }
# }
# layout['title'] = "Title"
#
# def get_df_code_name(code_name=None):
#     # code name to code
#     # df_sl = fdr.StockListing("KRX")
#     # print(df_sl.head())
#     # print(df_sl.columns)
#     df = fdr.StockListing('KRX')[['Name', 'Symbol', 'Market']]  # 코스피, 코스닥, 코넥스 전체
#     df.columns = ['code_name', 'code', 'market']
#
#     # 입력되는 code name을 df 에서 검색 후 code 얻어옴.
#     code = df.loc[df['code_name'] == code_name]['code'].values[0]
#     df_code = fdr.DataReader(code, '2019-01-02')
#
#     # print(df_code.tail())
#
#     # print(stocks[['Symbol', 'Market', 'Name']].head())
#     # print(df.columns)
#
#     return df_code
#
# df = get_df_code_name("삼성전자")
#
# df_1 = cf.datagen.lines()
# print(df_1.head())
#
# df_1.iplot(kind='line')

# fplt.plot(df, type='candle', title="삼성", ylabel='Price (won)')

# candlestick = go.Candlestick(
#                             x=df.index,
#                             open=df['Open'],
#                             high=df['High'],
#                             low=df['Low'],
#                             close=df['Close'],
#                             increasing_line_color='red', decreasing_line_color='blue',
#                             )
#
# fig = go.Figure(data=[candlestick])
#
# fig.update_layout(
#                 title="삼성",
#                 yaxis_title='주가(원)',
#                 xaxis_rangeslider_visible=False)
# fig.show()

# get_df_code_name('삼성전자')
#
# def get_price_hist(ticker):
#     # Put stock price data in dataframe
#     url = "https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={fro}&period2={to}&interval=1d&events=history".format(
#         ticker=ticker, fro=fro, to=to)
#     data = pd.read_csv(url)
#
#     # Convert date to timestamp and make index
#     data.index = data["Date"].apply(lambda x: pd.Timestamp(x))
#     data.drop("Date", axis=1, inplace=True)
#
#     return data
#
# def get_indicators(data):
#     # Get MACD
#     data["macd"], data["macd_signal"], data["macd_hist"] = talib.MACD(data['Close'])
#
#     # Get MA10 and MA30
#     data["ma10"] = talib.MA(data["Close"], timeperiod=10)
#     data["ma30"] = talib.MA(data["Close"], timeperiod=30)
#
#     # Get RSI
#     data["rsi"] = talib.RSI(data["Close"])
#     data['rsi_signal'] = talib.MA(data['rsi'], timeperiod=6)
#     return data
#
# def plot_chart(data, n, ticker):
#     # Filter number of observations to plot
#     data = data.iloc[-n:]
#
#     # Create figure and set axes for subplots
#     fig = plt.figure()
#     fig.set_size_inches((15, 16))
#     ax_candle = fig.add_axes((0, 0.72, 1, 0.32))
#     ax_macd = fig.add_axes((0, 0.48, 1, 0.2), sharex=ax_candle)
#     ax_rsi = fig.add_axes((0, 0.24, 1, 0.2), sharex=ax_candle)
#     ax_vol = fig.add_axes((0, 0, 1, 0.2), sharex=ax_candle)
#
#     # Format x-axis ticks as dates
#     ax_candle.xaxis_date()
#
#     # Get nested list of date, open, high, low and close prices
#     ohlc = []
#     for date, row in data.iterrows():
#         openp, highp, lowp, closep = row[:4]
#         ohlc.append([date2num(date), openp, highp, lowp, closep])
#
#     # Plot candlestick chart
#     ax_candle.plot(data.index, data["ma10"], label="MA10")
#     ax_candle.plot(data.index, data["ma30"], label="MA30")
#     candlestick_ohlc(ax_candle, ohlc, colorup="r", colordown="b", width=0.8)
#     ax_candle.legend()
#     ax_candle.set_ylabel('test')
#
#     # Plot MACD
#     ax_macd.plot(data.index, data["macd"], label="macd")
#     ax_macd.bar(data.index, data["macd_hist"] * 3, label="hist")
#     ax_macd.plot(data.index, data["macd_signal"], label="signal")
#     ax_macd.legend()
#
#     # Plot RSI
#     # Above 70% = overbought, below 30% = oversold
#     ax_rsi.set_ylabel("(%)")
#     ax_rsi.plot(data.index, [70] * len(data.index), label="overbought")
#     ax_rsi.plot(data.index, [30] * len(data.index), label="oversold")
#     ax_rsi.plot(data.index, data["rsi"], label="rsi")
#     ax_rsi.plot(data.index, data["rsi_signal"], label="signal(6)")
#     ax_rsi.legend()
#
#     # Show volume in millions
#     ax_vol.bar(data.index, data["Volume"] / 1000000)
#     ax_vol.set_ylabel("(Million)")
#
#     # Save the chart as PNG
#     fig.savefig("charts/" + ticker + ".png", bbox_inches="tight")
#
#     plt.show()
#
# nflx_df = get_price_hist("NFLX")
# # nflx_df2 = get_indicators(nflx_df)
# df = get_df_code_name('삼성전자')
# df2 = get_indicators(df)
# # plot_chart(nflx_df2, 180, "NFLX")
# plot_chart(df2, 180, "삼성전자")