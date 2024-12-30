# Import required libraries
import requests
import pandas as pd
import json

# Function to fetch jokes from the Official Joke API
def fetch_jokes(api_url):
    """
    Fetch jokes from the Official Joke API and return as a pandas DataFrame.
    :param api_url: URL of the API
    :return: Pandas DataFrame containing jokes
    """
    try:
        # Sending GET request to the API
        response = requests.get(api_url)
        response.raise_for_status()  # Raise HTTPError for bad responses

        # Parse JSON response
        jokes = json.loads(response.text)

        # Convert JSON data into pandas DataFrame
        df = pd.DataFrame(jokes)

        # Drop unnecessary columns (type and id)
        df = df.drop(columns=["type", "id"])

        return df
    except requests.exceptions.RequestException as e:
        print(f"Error fetching jokes: {e}")
        return pd.DataFrame()

# Main execution block
if __name__ == "__main__":
    # URL of the Official Joke API
    api_url = "https://official-joke-api.appspot.com/jokes/ten"

    print("Fetching jokes from the Official Joke API...")
    jokes_data = fetch_jokes(api_url)

    # Display the DataFrame
    if not jokes_data.empty:
        print("\nJokes DataFrame:")
        print(jokes_data)

        # Optionally save the jokes to a CSV file
        jokes_data.to_csv("jokes.csv", index=False)
        print("\nJokes saved to 'jokes.csv'.")
    else:
        print("No jokes retrieved.")
