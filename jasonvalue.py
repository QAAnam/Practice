import json

# Open the JSON file
with open('C:\\Users\\anam.kumar\\PycharmProjects\\First\\TEST.json', encoding='UTF-8') as f:
    # Load the JSON data into a Python dictionary
    data = json.load(f)

for i in range(len(data['subMenus'][0]['quickCombos'])):
 value = data['subMenus'][0]['quickCombos'][i]['itemId']
 print(value)
