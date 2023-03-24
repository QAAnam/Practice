import copy
import json
import random
from jsonpath_ng import jsonpath, parse
import jsonschema
import requests

with open('Sides_And_Desserts_payload.json', encoding='UTF-8') as f:
    payloads = json.load(f)
with open('ExpectedSchema.json', 'r') as f:
    ExpectedSchema=json.load(f)

RawDataFromSucessOrderResponse=[]
SucessOrderResponse=[]
FailedOrderResponseWithStatusCode=[]
FailedOrderResponseWithStatusCodeCheck=False
FailedOrderResponseWithResponseSchema=[]
FailedOrderResponseWithResponseSchemaCheck=False

for payload in payloads:
    CONfigpayload = copy.deepcopy(payload)
    ExternalId = str(random.randint(999999999,99999999999))
    CONfigpayload['code']= ExternalId
    CONfigpayload['token']= f"17011167{ExternalId}-_-oma_a3fcd207-8bcc-5641-bbf6-7ac37207f031-_-me-ae"
    url = "https://talabat-qa.americanarest.com/aggregatororder-service/v20/tb/order/KFC_UAE_1222"
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzZXJ2aWNlIjoibWlkZGxld2FyZSIsImlhdCI6MTY2NDE5MTM3MX0.tiXEt5QLGt9bVIEstmg4cTSJ0yPtlZ2z8tdY5ZRgLtnv_OqmnhueIGhD_0Kdq4dqF2mtx1a0mldbOWRc-6AH5g',
               'brand': 'KFC',
               }
    RequstBody=json.dumps(CONfigpayload)
    #print(RequstBody)
    response = requests.post(url, data=RequstBody, headers=headers)
    if response.status_code==200:
        try:
            RawDataFromSucessOrderResponse.append(response.json())
            CONfigResponse = response.json()
            #**********Verify json schema of respone and modify response a/c ******************
            jsonschema.validate(instance=CONfigResponse, schema=ExpectedSchema)
            CONfigResponse['remoteOrderId']=CONfigResponse['remoteResponse'].get('remoteOrderId')
            CONfigResponse['Status code']= response.status_code
            CONfigResponse['External ID']= CONfigpayload.get('code')
            CONfigResponse['Total Price']= CONfigpayload['price'].get('grandTotal')
            CONfigResponse['subTotal']= CONfigpayload['price'].get('subTotal')
            CONfigResponse['deliveryFee']= CONfigpayload['price'].get('deliveryFee')
            CONfigResponse.pop('remoteResponse')
            SucessOrderResponse.append(CONfigResponse)
            #print("Congratulations! The response JSON schema was validated successfully.")
        except jsonschema.exceptions.ValidationError as e:
            FailedOrderResponseWithResponseSchemaCheck=True
            FailedOrderResponseWithResponseSchema.append(response.json())
            print(f"Validation failed: {e}")
    else:
        FailedOrderResponseWithStatusCodeCheck=True
        FailedOrderResponseWithStatusCode.append(response.json())
#print(SucessOrderResponse)
with open('SucessOrderResponse.json', 'w',encoding='utf8') as f:
    json.dump(SucessOrderResponse, f, ensure_ascii=False, indent=4)
with open('RawDataFromSucessOrderResponse.json', 'w',encoding='utf8') as f:
    json.dump(RawDataFromSucessOrderResponse, f, ensure_ascii=False, indent=4)
if FailedOrderResponseWithStatusCodeCheck:
    with open('FailedOrderResponseWithStatusCode.json', 'w', encoding='utf8') as f:
        json.dump(FailedOrderResponseWithStatusCode, f, ensure_ascii=False, indent=4)
if FailedOrderResponseWithResponseSchemaCheck:
    with open('FailedOrderResponseWithResponseSchema.json', 'w', encoding='utf8') as f:
        json.dump(FailedOrderResponseWithResponseSchema, f, ensure_ascii=False, indent=4)