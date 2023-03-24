import json

# Open the JSON file

with open('C:\\Users\\anam.kumar\\PycharmProjects\\First\\Menu - Copy [MConverter.eu].json', encoding='UTF-8') as f:
    # Load the JSON data into a Python dictionary
    data = json.load(f)

for i in range(len(data[0]['subMenus'][3]['items'])):
    if not data[0]['subMenus'][3]['items'][i]['modifierGroups']:
        value = data[0]['subMenus'][3]['items'][i]


    else:
        value=data[0]['subMenus'][3]['items'][i]
        value.append(data[0]['subMenus'][3]['items'][i]['modifierGroups'][0])
    print(value)




