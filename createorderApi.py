import json
import requests
import  random
# First JSON object
with open('C:\\Users\\anam.kumar\\PycharmProjects\\First\\OmanKFCPayload.json', encoding='UTF-8') as f:
    # Load the JSON data into a Python dictionary
    data1 = json.load(f)
with open('C:\\Users\\anam.kumar\\PycharmProjects\\First\\itemdetails.json', encoding='UTF-8') as g:
    # Load the JSON data into a Python dictionary
    data2 = json.load(g)
    data3=data2['itemDetails'][0]
data1['itemDetails'].append(data2['itemDetails'][0])
data1['itemDetails'].append(data2['itemDetails'][len(data2['itemDetails'])-1])
data = data1
# Second JSON object
data['noteDetails'][0]['text'] = random.randint(100000000, 1000000000000)
# Convert the data dictionary to a JSON string
exid = data1['noteDetails'][0]['text']
payload = json.dumps(data)

print(payload)

# Make a POST request with the payload
url = "https://online-ordering-channel-eapi-staging-v1.de-c1.cloudhub.io/api/orders?customerId=656496&conceptId=3"
headers = {'Content-Type': 'application/json',
           'x-client_id':  '9feec1249d404765a92081ae816e0efa',
           'x-country_id': '5',
           'x-client_secret': 'a57Ab53Cfdfe46a998665271902342da'
           }
response = requests.post(url, data=payload, headers=headers)
Response=[]
response=response.json()
print(response)
print("***************************************************************************************************************")
print(response)
response['wwww' ]= 'eee'
Response.append(response)
# Print the response from the server
with open('1responsecreated.json','w',encoding='utf-8') as f:
    json.dump(Response, f, ensure_ascii=False, indent=4)

print(exid)
