# import json
#
# with open('sanjeev.json', encoding="utf8") as f:
#     menu_data = json.load(f)
# working code
# for menu in menu_data:
#     for submenu in menu['subMenus']:
#         if submenu.get('quickCombos'):
#             for combo in submenu['quickCombos']:
#                 print(combo['name'])
#                 print(combo['itemId'])
#                 for modifier_group in combo['modifierGroups']:
#                     if modifier_group['name'] == 'Choice of Side Item':
#                         for modifier_item in modifier_group['modifierItems']:
#                             print(modifier_item['name'])
#                             print(modifier_item['priceInclusive'])

# working code
# import json
#
# with open('sanjeev.json', encoding="utf8") as f:
#     menu_data = json.load(f)
#
# for menu in menu_data:
#     for submenu in menu['subMenus']:
#         if submenu.get('quickCombos'):
#             for combo in submenu['quickCombos']:
#                 print(combo['name'])
#                 print(combo['itemId'])
#                 for modifier_group in combo['modifierGroups']:
#                     if modifier_group['name'] == 'Choice of Side Item':
#                         for modifier_item in modifier_group['modifierItems']:
#                             print('Side item:', modifier_item['name'])
#                             print('Price:', modifier_item['priceInclusive'])
#                 for modifier_group in combo['modifierGroups']:
#                     if modifier_group['name'] == 'Choice of Beverages':
#                         for modifier_item in modifier_group['modifierItems']:
#                             print('Beverage:', modifier_item['name'])
#                             print('Price:', modifier_item['priceInclusive'])


# import json
#
# with open('sanjeev.json', encoding="utf8") as f:
#     menu_data = json.load(f)
#
# side_items = set()
#
# for menu in menu_data:
#     for submenu in menu['subMenus']:
#         if submenu.get('quickCombos'):
#             for combo in submenu['quickCombos']:
#                 for modifier_group in combo['modifierGroups']:
#                     if modifier_group.get('name') == 'Choice of Side Item':
#                         for modifier_item in modifier_group['modifierItems']:
#                             side_items.add(modifier_item['name'])
#
# print('Unique Side Items:', side_items)
#
# for menu in menu_data:
#     for submenu in menu['subMenus']:
#         if submenu.get('quickCombos'):
#             for combo in submenu['quickCombos']:
#                 combo_side_items = set()
#                 for modifier_group in combo['modifierGroups']:
#                     if modifier_group.get('name') == 'Choice of Side Item':
#                         for modifier_item in modifier_group['modifierItems']:
#                             combo_side_items.add(modifier_item['name'])
#                 if combo_side_items:
#                     print('Combo:', combo['name'])
#                     print('Side Items:', combo_side_items)

# with all permutation nd combinations of all sides items
# import itertools
# import json
#
# with open('sanjeev.json', encoding="utf8") as f:
#     menu_data = json.load(f)
#
# combos_data = []
#
# # Loop through all combos
# for menu in menu_data:
#     for submenu in menu['subMenus']:
#         if submenu.get('quickCombos'):
#             for combo in submenu['quickCombos']:
#                 combo_data = {
#                     'combo_name': combo['name'],
#                     'combo_id': combo['itemId'],
#                     'side_items': []
#                 }
#                 # Loop through all modifier groups of the combo
#                 for modifier_group in combo['modifierGroups']:
#                     if modifier_group['name'] == 'Choice of Side Item':
#                         # Loop through all modifier items of the modifier group
#                         for modifier_item in modifier_group['modifierItems']:
#                             combo_data['side_items'].append({
#                                 'name': modifier_item['name'],
#                                 'price': modifier_item['priceInclusive']
#                             })
#                 combos_data.append(combo_data)
#
# # Loop through all combos data to generate side items combinations
# for combo_data in combos_data:
#     print('Combo:', combo_data['combo_name'])
#     side_items = combo_data['side_items']
#     print('Side Items:')
#     for i in range(1, len(side_items) + 1):
#         for combination in itertools.combinations(side_items, i):
#             print([item['name'] for item in combination])
#     print('------------------------------------')

# generate payload in americana structure success code
# import json
# import csv
#
# with open('sanjeev.json', encoding='utf8') as f:
#     menu_data = json.load(f)
#
# combo_list = []
#
# for menu in menu_data:
#     for submenu in menu['subMenus']:
#         if submenu.get('quickCombos'):
#             for combo in submenu['quickCombos']:
#                 combo_dict = {}
#                 combo_dict['name'] = combo['name']
#                 combo_dict['itemId'] = combo['itemId']
#                 combo_dict['itemType'] = combo['itemType']
#                 combo_dict['price'] = combo['priceInclusive']
#                 combo_dict['modeCode'] = "1"
#                 combo_dict['level'] = "0"
#                 combo_dict['orderMode'] = "1"
#                 modifier_list = []
#                 has_beverages = False
#                 for modifier_group in combo['modifierGroups']:
#                     if modifier_group['name'] == 'Choice of Side Item':
#                         for modifier_item in modifier_group['modifierItems']:
#                             modifier_dict = {}
#                             modifier_dict['name'] = modifier_item['name']
#                             modifier_dict['itemId'] = modifier_item['itemId']
#                             if 'itemType' in modifier_item:
#                                 modifier_dict['itemType'] = modifier_item['itemType']
#                             else:
#                                 modifier_dict['itemType'] = ''
#                             modifier_dict['price'] = modifier_item['priceInclusive']
#                             modifier_dict['modeCode'] = "1"
#                             modifier_dict['level'] = "0"
#                             modifier_dict['groupId'] = modifier_group.get('groupId', '')
#                             modifier_dict['orderMode'] = "1"
#                             modifier_dict['parentItemId'] = None
#                             modifier_list.append(modifier_dict)
#                     elif modifier_group['name'] == 'Choice of Beverages':
#                         has_beverages = True
#                         for modifier_item in modifier_group['modifierItems']:
#                             modifier_dict = {}
#                             modifier_dict['name'] = modifier_item['name']
#                             modifier_dict['itemId'] = modifier_item['itemId']
#                             if 'itemType' in modifier_item:
#                                 modifier_dict['itemType'] = modifier_item['itemType']
#                             else:
#                                 modifier_dict['itemType'] = ''
#                             modifier_dict['price'] = modifier_item['priceInclusive']
#                             modifier_dict['modeCode'] = "1"
#                             modifier_dict['level'] = "0"
#                             modifier_dict['groupId'] = modifier_group.get('groupId', '')
#                             modifier_dict['orderMode'] = "1"
#                             modifier_dict['parentItemId'] = None
#                             modifier_list.append(modifier_dict)
#                 if not has_beverages:
#                     modifier_list.append({'groupId': 'Choice of Beverages', 'name': 'No Beverages', 'price': 0, 'itemId': 0, 'itemType': '', 'modeCode': '1', 'level': '0', 'orderMode': '1', 'parentItemId': None})
#                 combo_dict['item-modifiers'] = modifier_list
#                 combo_list.append(combo_dict)
#
# # Write the output to a JSON file
# with open('sanjeev_output.json', 'w', encoding='utf8') as f:
#     json.dump(combo_list, f, ensure_ascii=False, indent=4)
###########################################################################
import json

with open('sanjeev.json', encoding='utf8') as f:
    menu_data = json.load(f)

combo_list = []

for menu in menu_data:
    for submenu in menu['subMenus']:
        if submenu.get('quickCombos'):
            for combo in submenu['quickCombos']:
                combo_dict = {}
                combo_dict['name'] = combo['name']
                combo_dict['itemId'] = combo['itemId']
                combo_dict['itemType'] = combo['itemType']
                combo_dict['price'] = combo['priceInclusive']
                combo_dict['modeCode'] = "1"
                combo_dict['level'] = "0"
                combo_dict['orderMode'] = "1"
                modifier_groups = {group['name']: group for group in combo['modifierGroups']}
                if 'Choice of Side Item' not in modifier_groups or 'Choice of Beverages' not in modifier_groups:
                    continue
                side_items = modifier_groups['Choice of Side Item']['modifierItems']
                beverages = modifier_groups['Choice of Beverages']['modifierItems']
                for side_item in side_items:
                    for beverage in beverages:
                        combo_with_modifiers = combo_dict.copy()
                        combo_with_modifiers['item-modifiers'] = [
                            {
                                'name': side_item['name'],
                                'itemId': side_item['itemId'],
                                'itemType': side_item.get('itemType', ''),
                                'price': side_item['priceInclusive'],
                                'modeCode': '1',
                                'level': '0',
                                'groupId': modifier_groups.get('Choice of Side Item', {}).get('groupId', ''),
                                'orderMode': '1',
                                'parentItemId': combo_dict['itemId']
                            },
                            {
                                'name': beverage['name'],
                                'itemId': beverage['itemId'],
                                'itemType': beverage.get('itemType', ''),
                                'price': beverage['priceInclusive'],
                                'modeCode': '1',
                                'level': '0',
                                'groupId': modifier_groups.get('Choice of Beverages', {}).get('groupId', ''),
                                'orderMode': '1',
                                'parentItemId': combo_dict['itemId']
                            }
                        ]
                        combo_list.append(combo_with_modifiers)

# Write the output to a JSON file
with open('sanjeev_output.json', 'w', encoding='utf8') as f:
    json.dump(combo_list, f, ensure_ascii=False, indent=4)
