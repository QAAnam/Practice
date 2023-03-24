import json
from itertools import product

with open('kfc_uae_transformed.json', encoding='utf8') as f:
    menu_data = json.load(f)

# Initialize list to store product combinations
products = []

# Loop through dictionary and extract items from 'Drinks' category
for category in menu_data['categories']:
    category_name = category['englishName']
    if category_name == 'Sides & Desserts':
        for item in category['items']:
            # Create a list of all choice options for the item
            choice_options = []
            for choice_category in item.get('choiceCategories', []):
                choice_options.append([choice['englishName'] for choice in choice_category.get('choices', [])])
            # Loop through all combinations of choice options and add to products list
            for choice_combination in product(*choice_options):
                choice_prices = []
                for choice in choice_combination:
                    for choice_category in item.get('choiceCategories', []):
                        for ch in choice_category.get('choices', []):
                            #print(ch)
                            if ch['englishName'] == choice:
                                choice_prices.append(ch.get('price', 0))
                if choice_prices:
                    unit_price = item.get('price', 0) + sum(choice_prices)
                else:
                    unit_price = item.get('price', 0)
                product_data = {
                    'id': str(hash(item['englishName'] + ''.join(choice_combination))),
                    'remoteCode': item['id'],
                    'name': item['englishName'],
                    'description': item.get('englishDescription', ''),
                    'comment': '',
                    'categoryName': None,
                    'variation': {
                        'name': item['englishName']
                    },
                    'unitPrice': unit_price,
                    'paidPrice': '',
                    'discountAmount': '',
                    'quantity': '1',
                    'halfHalf': False,
                    'vatPercentage': '',
                    'selectedChoices': [
                        {'name': choice} for choice in choice_combination
                    ],
                    'selectedToppings': []
                }
                products.append(product_data)

# Print the final products list in JSON format
print(json.dumps({'products': products}, indent=4))

# Output the list of products as a JSON file
with open(f'{category_name}_products.json', 'w', encoding='utf8') as f:
    json.dump(products, f, ensure_ascii=False, indent=4)

# Output the list of products as a text file
with open(f'{category_name}_products.txt', 'w', encoding='utf8') as f:
    for product in products:
        f.write(str(product) + '\n')
