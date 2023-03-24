import json
import random
import requests

with open('C:\\Users\\anam.kumar\\PycharmProjects\\First\\Experimented.json', encoding='UTF-8') as f:
    # Load the JSON data into a Python dictionary
    nested_json1 = json.load(f)
nested_json={
    "id": "123",
    "name": "Example",
    "items": [
        {
            "id": "456",
            "name": "Item 1",
            "choiceCategories": []
        },
        {
            "id": "789",
            "name": "Item 2",
            "choiceCategories": [
                {
                    "id": "111",
                    "name": "Category 1",
                    "options": [
                        {
                            "id": "222",
                            "name": "Option 1",
                            "choiceCategories": []
                        }
                    ]
                }
            ]
        },
        {
            "id": "321",
            "name": "Item 3",
            "choiceCategories": []
        }
    ]
}
def find_dicts_with_empty_choiceCategories(nested_dict, parent_dict=None):
    result = []
    if isinstance(nested_dict, dict):
        if nested_dict.get("choiceCategories") == []:
            result.append((nested_dict, parent_dict))
        for key, value in nested_dict.items():
            result.extend(find_dicts_with_empty_choiceCategories(value, nested_dict))
    elif isinstance(nested_dict, list):
        for item in nested_dict:
            result.extend(find_dicts_with_empty_choiceCategories(item, parent_dict))
    return result

result = find_dicts_with_empty_choiceCategories(nested_json1)
print(result)

with open('C:\\Users\\anam.kumar\\PycharmProjects\\First\\Talabat_Base.json', encoding='UTF-8') as f:
    # Load the JSON data into a Python dictionary
    data1 = json.load(f)
#with open('C:\\Users\\anam.kumar\\PycharmProjects\\First\\itemdetails.json', encoding='UTF-8') as g:
    # Load the JSON data into a Python dictionary
#    data2 = json.load(g)
    data3=result[0]
    data2=data3
data1['products'].append(data2)
#data1['itemDetails'].append(data2['itemDetails'][len(data2['itemDetails'])-1])
data = data1
# Second JSON object
data['token'] = str(random.randint(100000000, 1000000000000))+"-_-oma_a3fcd207-8bcc-5641-bbf6-7ac37207f031-_-me-ae"
# Convert the data dictionary to a JSON string
exid = data1['code']
payload = json.dumps(data)

print(payload)

# Make a POST request with the payload
url = "https://talabat-qa.americanarest.com/aggregatororder-service/v20/tb/order/KFC_UAE_1219"
headers = {'Content-Type': 'application/json',
           'Authorization':  'Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzZXJ2aWNlIjoibWlkZGxld2FyZSIsImlhdCI6MTY2NDE5MTM3MX0.tiXEt5QLGt9bVIEstmg4cTSJ0yPtlZ2z8tdY5ZRgLtnv_OqmnhueIGhD_0Kdq4dqF2mtx1a0mldbOWRc-6AH5g',
           'brand': 'HRD',
           }
#           'x-client_secret': 'a57Ab53Cfdfe46a998665271902342da'

response = requests.post(url, data=payload, headers=headers)

# Print the response from the server
#print(response.content)

print(exid)
#find_dict_with_empty_choiceCategories(nested_json1)
