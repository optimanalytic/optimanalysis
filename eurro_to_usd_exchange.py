import datetime
import pandas_datareader as pdr
import plotly.express as px

# Defining the start and end dates for the data retrieval
start_date = datetime.datetime(2024, 7, 1)  # Start date: July 1, 2024
end_date = datetime.datetime(2024, 12, 18)  # End date: December 18, 2024

# Fetching historical daily exchange rates for EUR to USD using pandas_datareader
# 'DEXUSEU' is the code for the Euro to US Dollar exchange rate from FRED
eur_to_usd_data = pdr.get_data_fred('DEXUSEU', start_date, end_date)

# Resetting index to have dates as a separate column and rename columns for clarity
eur_to_usd_data.reset_index(inplace=True)
eur_to_usd_data.columns = ['Date', 'DEXUSEU']

# Printing the entire DataFrame
print(eur_to_usd_data)

# Plotting the data using Plotly Express
# Creating a line plot with the fetched data, plotting 'Date' on the x-axis and 'DEXUSEU' on the y-axis
fig = px.line(eur_to_usd_data, x='Date', y='DEXUSEU', title='EUR to USD Exchange Rate (2024)')

# Showing the plot
fig.show()
