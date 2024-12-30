# This code is part of the IBM Data Engineering Professional Certificate course on Coursera
# © IBM Corporation. All rights reserved.

# Import required libraries
import requests
import pandas as pd
import json

# Function to fetch and normalize Fruityvice API data
def fetch_fruityvice_data(api_url):
    """
    Fetch fruit data from Fruityvice API, normalize JSON, and return a DataFrame.
    :param api_url: URL of the Fruityvice API endpoint
    :return: Pandas DataFrame containing normalized fruit data
    """
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        response.raise_for_status()  # Raise HTTPError for bad responses

        # Parse JSON response
        results = json.loads(response.text)

        # Normalize nested JSON data
        df = pd.json_normalize(results)
        return df
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return pd.DataFrame()

# Main execution block
if __name__ == "__main__":
    # URL of the Fruityvice API
    api_url = "https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all"

    print("Fetching Fruityvice data...")
    fruit_data = fetch_fruityvice_data(api_url)

    # Display the DataFrame
    if not fruit_data.empty:
        print("\nFruityvice DataFrame:")
        print(fruit_data.head())

        # Extract specific information (Family and Genus of Cherry)
        cherry_info = fruit_data.loc[fruit_data["name"] == "Cherry", ["family", "genus"]]
        if not cherry_info.empty:
            print("\nCherry Information:")
            print(cherry_info)

        # Find out how many calories are in a banana
        banana_info = fruit_data.loc[fruit_data["name"] == "Banana", ["nutritions.calories"]]
        if not banana_info.empty:
            print("\nBanana Calories:")
            print(f"Calories in a Banana: {banana_info.iloc[0]['nutritions.calories']}")
    else:
        print("No data retrieved.")
