import json
import requests

# First JSON object
data1 = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Second JSON object
data2 = {
    "email": "john@example.com",
    "phone": "1234567890"
}

# Joining two JSON objects
data = {**data1, **data2}

# Convert the data dictionary to a JSON string
payload = json.dumps(data)
print(payload)

# Make a POST request with the payload
url = "http://localhost:3000/profile"
headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=payload, headers=headers)

# Print the response from the server
print(response.status_code)
