import json
from itertools import product

with open('kfc_uae_transformed.json', encoding='utf8') as f:
    menu_data = json.load(f)

# Initialize list to store product combinations
products = []

# Loop through dictionary and extract items from 'Drinks' category
for category in menu_data['categories']:
    category_name = category['englishName']
    if category_name == 'For Sharing':
        for item in category['items']:
            print()
            print()
            print(item.get('id'))
            print()
            for choiceCategories in item:
                print(choiceCategories)
                for choices in item['choiceCategories']:
                    print(item['choiceCategories'][0].get('choices'))
                    for choiceCategories in choices:
                        print(choiceCategories)
#        try:            print(item['choiceCategories'][0].get('choices'))
 #       except:            print(item.get('choiceCategories'))