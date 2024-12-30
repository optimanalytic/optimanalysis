# Importing libraries
import requests
import pandas as pd
import plotly.express as px
from io import StringIO

# Your Alpha Vantage API key
api_key = 'your_alpha_vantage_api_key'


# Functioning to get the exchange rate data from Alpha Vantage
def get_nok_to_usd(api_key):
    url = f'https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=NOK&to_symbol=USD&apikey={api_key}&datatype=csv'
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Decode the content and use StringIO to read it as a CSV
        data = pd.read_csv(StringIO(response.content.decode('utf-8')))
        return data
    else:
        print(f"Error fetching data: {response.status_code}")
        return None


# Fetching the NOK to USD exchange rate data
nok_to_usd_data = get_nok_to_usd(api_key)

if nok_to_usd_data is not None:
    # Convert 'timestamp' to datetime
    nok_to_usd_data['timestamp'] = pd.to_datetime(nok_to_usd_data['timestamp'])

    # Renaming columns for clarity
    nok_to_usd_data.columns = ['Date', 'Open', 'High', 'Low', 'Close']

    # Printing the DataFrame
    print(nok_to_usd_data)

    # Plotting the data using Plotly Express
    fig = px.line(nok_to_usd_data, x='Date', y='Close', title='NOK to USD Exchange Rate')
    fig.show()
