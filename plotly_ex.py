import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import FinanceDataReader as fdr

# data
code_df = fdr.StockListing('KRX')[['Name', 'Symbol']]
code_df.columns = ['code_name', 'code']
print((code_df.head()))

def get_code(df, code_name="삼성전자"):
    return df.loc[df['code_name'] == code_name]['code'].values[0]

code_name = "삼성전자"
start_date = "2019-01-02"
df = fdr.DataReader(get_code(code_df, code_name='삼성전자'), start_date)
df = df.reset_index()
print(df.head())

# Create subplots and mention plot grid size
fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
               vertical_spacing=0.03, subplot_titles=('OHLC', 'Volume'),
               row_width=[0.2, 0.7])

# Plot OHLC on 1st row
fig.add_trace(go.Candlestick(x=df["Date"], open=df["Open"], high=df["High"],
                low=df["Low"], close=df["Close"], name="OHLC"),
                row=1, col=1
)

# Bar trace for volumes on 2nd row without legend
fig.add_trace(go.Bar(x=df['Date'], y=df['Volume'], showlegend=False), row=2, col=1)

# Do not show OHLC's rangeslider plot
fig.update(layout_xaxis_rangeslider_visible=False)
fig.show()