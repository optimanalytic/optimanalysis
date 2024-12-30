import numpy as np
import pandas as pd

# You can also use this section to suppress warnings generated by your code:
def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')

# Define the URL for extracting GDP data
URL = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

# Step 1: Extract tables from the webpage using Pandas. Retain table number 3 as the required dataframe.
tables = pd.read_html(URL)
df = tables[3]

# Step 2: Replace the column headers with column numbers
df.columns = range(df.shape[1])

# Step 3: Retain columns with index 0 and 2 (name of country and value of GDP quoted by IMF)
df = df[[0, 2]]

# Step 4: Retain rows with index 1 to 10, indicating the top 10 economies of the world
df = df.iloc[1:11, :]

# Step 5: Assign column names as "Country" and "GDP (Million USD)"
df.columns = ['Country', 'GDP (Million USD)']

# Step 6: Change the data type of the 'GDP (Million USD)' column to integer
df['GDP (Million USD)'] = df['GDP (Million USD)'].astype(int)

# Step 7: Convert the GDP value in Million USD to Billion USD
df['GDP (Million USD)'] = df['GDP (Million USD)'] / 1000

# Step 8: Use numpy.round() method to round the value to 2 decimal places
df['GDP (Million USD)'] = np.round(df['GDP (Million USD)'], 2)

# Step 9: Rename the column header from 'GDP (Million USD)' to 'GDP (Billion USD)'
df.rename(columns={'GDP (Million USD)': 'GDP (Billion USD)'}, inplace=True)

# Step 10: Save the DataFrame to a CSV file named "Largest_economies.csv"
df.to_csv('./Largest_economies.csv', index=False)

# Display a confirmation message
print("The DataFrame has been successfully saved to 'Largest_economies.csv'")

# Note: This script processes GDP data as part of an exercise in the IBM Data Engineering Professional Certificate course.
