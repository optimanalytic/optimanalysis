# This code is part of the IBM Data Engineering Professional Certificate course on Coursera
# © IBM Corporation. All rights reserved.

# Import required libraries
from randomuser import RandomUser
import pandas as pd
import requests


# Define a function to get user data and store it in a structured format
def get_users(num_users=10):
    """
    Generate random user data and return it as a Pandas DataFrame.
    :param num_users: Number of random users to generate
    :return: Pandas DataFrame containing user data
    """
    users = []
    try:
        # Generate random users
        random_users = RandomUser.generate_users(num_users)
        for user in random_users:
            users.append({
                "Name": user.get_full_name(),
                "Gender": user.get_gender(),
                "City": user.get_city(),
                "State": user.get_state(),
                "Email": user.get_email(),
                "DOB": user.get_dob(),
                "Picture": user.get_picture()
            })
    except Exception as e:
        print(f"Error generating users: {e}")
    return pd.DataFrame(users)


# Main execution block
if __name__ == "__main__":
    # Generate data for 10 random users
    print("Generating random user data...")
    user_data = get_users(10)

    # Display the DataFrame
    print("\nRandom Users DataFrame:")
    print(user_data)

    # Save DataFrame to a CSV file
    csv_file_path = "random_users.csv"
    try:
        user_data.to_csv(csv_file_path, index=False)
        print(f"\nUser data saved to {csv_file_path}")
    except Exception as e:
        print(f"Error saving CSV file: {e}")

    # Download and save user profile pictures
    print("\nDownloading user profile pictures...")
    for index, row in user_data.iterrows():
        image_url = row['Picture']
        file_name = f"user_{index + 1}.jpg"
        try:
            response = requests.get(image_url, stream=True)
            if response.status_code == 200:
                with open(file_name, 'wb') as img_file:
                    for chunk in response.iter_content(1024):
                        img_file.write(chunk)
                print(f"Saved: {file_name}")
            else:
                print(f"Failed to download image for {row['Name']}")
        except Exception as e:
            print(f"Error downloading image for {row['Name']}: {e}")
