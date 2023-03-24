import json

with open('C:\\Users\\anam.kumar\\PycharmProjects\\First\\BasePayload.json', encoding='UTF-8') as f:
    # Load the JSON data into a Python dictionary
    BasePayload = json.load(f)
with open('C:\\Users\\anam.kumar\\PycharmProjects\\First\\hrd_uae_menu_output_V7.json', encoding='UTF-8') as g:
    # Load the JSON data into a Python dictionary
    Baseproduct = json.load(g)
i=0
k=0
for choiceCategories in  Baseproduct['categories'][0]['items'][0]['choiceCategories']:
    for choices in Baseproduct['categories'][0]['items'][0]['choiceCategories'][i]['choices']:
        print(Baseproduct['categories'][0]['items'][0]['choiceCategories'][i]['choices'][k])

        k=k+1
    i = i + 1