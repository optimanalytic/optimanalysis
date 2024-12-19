# Importing the yfinance library as yf for downloading financial data
import yfinance as yf
import plotly.graph_objects as go

# Setting the cryptocurrency symbol and date range
symbol = 'BTC-USD'         # Symbol for Bitcoin in USD
start_date = '2024-01-01'  # Start date for historical data
end_date = '2024-12-18'    # End date for historical data

# Fetching historical cryptocurrency data using yfinance
crypto_data = yf.download(symbol, start=start_date, end=end_date)

# Resetting the index to move the date from the index to a column
df = crypto_data.reset_index()
# Reset the DataFrame index, making the 'Date' a column

# Printing the DataFrame to inspect the data
print(df)
# Output the DataFrame to the console

# Plotting the data as a candlestick chart using Plotly
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open'],
                                     high=df['High'],
                                     low=df['Low'],
                                     close=df['Close'])])

# Adding title and labels to the plot
fig.update_layout(title=f'{symbol} Candlestick Chart',
                  xaxis_title='Date',
                  yaxis_title='Price (USD)',
                  xaxis_rangeslider_visible=False)

# Showing the plot
fig.show()