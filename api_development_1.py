# This code is part of the IBM Data Engineering Professional Certificate course on Coursera

from pycoingecko import CoinGeckoAPI
import pandas as pd
import plotly.graph_objects as go

# Initialize CoinGeckoAPI
cg = CoinGeckoAPI()

# Fetch Bitcoin data for the last 30 days
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)

# Convert the prices data into a DataFrame
data = pd.DataFrame(bitcoin_data['prices'], columns=['TimeStamp', 'Price'])

# Convert TimeStamp to datetime format
data['Date'] = pd.to_datetime(data['TimeStamp'], unit='ms')

# Create candlestick data by aggregating prices
candlestick_data = data.groupby(data.Date.dt.date).agg({
    'Price': ['min', 'max', 'first', 'last']
})

# Plot candlestick chart using Plotly
fig = go.Figure(data=[go.Candlestick(
    x=candlestick_data.index,
    open=candlestick_data['Price']['first'],
    high=candlestick_data['Price']['max'],
    low=candlestick_data['Price']['min'],
    close=candlestick_data['Price']['last']
)])

# Customize layout
fig.update_layout(
    xaxis_rangeslider_visible=False,
    xaxis_title='Date',
    yaxis_title='Price (USD $)',
    title='Bitcoin Candlestick Chart Over Past 30 Days'
)

# Show the chart
fig.show()
