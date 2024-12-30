# This code is part of the IBM Data Engineering Professional Certificate course on Coursera
# © IBM Corporation. All rights reserved.

import requests
import os
from PIL import Image
from IPython.display import IFrame


# Function to perform a GET request and display response details
def get_request_example():
    url = 'https://httpbin.org/get'
    payload = {"name": "Joseph", "ID": "123"}  # Query parameters

    # Sending GET request with query parameters
    response = requests.get(url, params=payload)

    print("GET Request URL:", response.url)
    print("Status Code:", response.status_code)
    print("Headers:", response.headers)
    print("Response Text:", response.text[:200])  # Printing a snippet of the response


# Function to perform a POST request and display response details
def post_request_example():
    url = 'https://httpbin.org/post'
    payload = {"name": "Joseph", "ID": "123"}  # Data for the POST request

    # Sending POST request
    response = requests.post(url, data=payload)

    print("POST Request URL:", response.url)
    print("Status Code:", response.status_code)
    print("Headers:", response.headers)
    print("Response JSON:", response.json())  # Printing JSON response


# Function to demonstrate saving an image from a URL
def save_image_example():
    image_url = 'https://via.placeholder.com/150'
    response = requests.get(image_url)

    if response.status_code == 200:
        image_path = os.path.join(os.getcwd(), 'image.png')
        with open(image_path, 'wb') as f:
            f.write(response.content)
        print(f"Image saved at {image_path}")
        Image.open(image_path).show()
    else:
        print("Failed to fetch the image.")


# Main execution
if __name__ == "__main__":
    print("--- GET Request Example ---")
    get_request_example()

    print("\n--- POST Request Example ---")
    post_request_example()

    print("\n--- Save Image Example ---")
    save_image_example()
