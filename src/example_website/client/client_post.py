import requests
import json

# URL of the API endpoint
url = 'http://127.0.0.1:5000/endpoint'

# Data to send in JSON format
data = {
    'key_niels': 'value_niels'
}

# Specify the content_format
headers = {'Content-type': 'application/json'}

# Send the POST request
response = requests.post(url, json=data, headers=headers)

# Print the response body (JSON content)
print(response.text)