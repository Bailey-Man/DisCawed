import requests

# Define the API endpoint URL
api_url = "https://api.foundrytabletop.com"

# Make a GET request to the API
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response content
    print(response.json())
else:
    # Print an error message
    print("Error connecting to the Foundry Tabletop API.")