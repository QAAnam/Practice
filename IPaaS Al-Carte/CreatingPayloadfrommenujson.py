import json
import copy
import requests
import  random
# First JSON object
with open('C:\\Users\\anam.kumar\\PycharmProjects\\First\\OmanKFCPayload.json', encoding='UTF-8') as f:
    # Load the JSON data into a Python dictionary
    BaseLoad = json.load(f)
    TempBaseLoad = copy.deepcopy(BaseLoad)
with open('C:\\Users\\anam.kumar\\PycharmProjects\\First\\itemdetails.json', encoding='UTF-8') as g:
    # Load the JSON data into a Python dictionary
    BaseItemDetails = json.load(g)
    TempBaseItemDetails = BaseItemDetails['itemDetails'][0]
with open('C:\\Users\\anam.kumar\\PycharmProjects\\First\\Menu - Copy [MConverter.eu].json', encoding='UTF-8') as h:
    # Load the JSON data into a Python dictionary
    MenuJson = json.load(h)
    i = 0
ItemS = []
for item in MenuJson[0]['subMenus'][3]['items']:
    TempMenuJson = MenuJson[0]['subMenus'][3]['items'][i]
    i = i+1
    # Loop over the keys in file2.json
    for key in TempMenuJson:
        # Check if the key exists in file1.json
        if key in TempBaseItemDetails:
            # Update the value in file1.json with the value from file2.json
            TempBaseItemDetails[key] = TempMenuJson[key]

    TempBaseLoad['itemDetails'].append(TempBaseItemDetails)
    ItemS.append(TempBaseItemDetails)
    data = TempBaseLoad
    # Second JSON object
    data['noteDetails'][0]['text'] = random.randint(100000000, 1000000000000)
    # Convert the data dictionary to a JSON string
    exid = TempBaseLoad['noteDetails'][0]['text']
    payload = json.dumps(data)

    print(payload)

    # Make a POST request with the payload
    url = "https://online-ordering-channel-eapi-staging-v1.de-c1.cloudhub.io/api/orders?customerId=656496&conceptId=3"
    headers = {'Content-Type': 'application/json',
               'x-client_id': '9feec1249d404765a92081ae816e0efa',
               'x-country_id': '5',
               'x-client_secret': 'a57Ab53Cfdfe46a998665271902342da'
               }
    response = requests.post(url, data=payload, headers=headers)

    # Print the response from the server
    print(response.content)

    print(exid)

    TempBaseLoad = copy.deepcopy(BaseLoad)
with open('itemdetailsoutput.json', 'w', encoding='utf8') as f:
    json.dump(ItemS, f, ensure_ascii=False, indent=4)

