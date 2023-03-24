import copy
import json

with open('kfc_uae_transformed.json', encoding='UTF-8') as f:
    MenuUAE = json.load(f)

with open('configurableItem.json', encoding='UTF-8') as f:
    BasePayload = json.load(f)
    BaseProduct = BasePayload['products'][0]
with open('sempleItem.json', encoding='UTF-8') as g:
    sempleItem = json.load(g)
    sempleItemProduct = sempleItem['products'][0]
with open('bundleItem.json', encoding='UTF-8') as g:
    bundleItem = json.load(g)
    bundleItemProduct = bundleItem['products'][0]

CONfigProductGenerated = []
itemhavinBDL =[]
Items_Not_Configured = 0
item_quanttity = "1"
choice_quanttity = 1
Selected_Topping_Type = "EXTRA"
item_comment = ""
item_categoryName = None
item_paidPrice = "0"
item_discountAmount = ""
item_halfHalf = False
item_vatPercentage = ""
BDLcount=0
SMPcount=0
CONcount=0
for category in MenuUAE['categories']:
    category_name = category['englishName']
    if category_name == 'For Sharing':
        for item in category['items']:
            if "|T:SMP".lower() in item.get('id').lower():
                SMPcount=SMPcount+1
                print("SMP",SMPcount)
                CONsempleItemProduct = copy.deepcopy(sempleItemProduct)
                CONfigitem_id = str(hash(item['englishName'] + ''.join(item)))
                CONsempleItemProduct['id'] = CONfigitem_id
                CONsempleItemProduct['remoteCode'] = item.get('id')
                CONsempleItemProduct['name'] = item.get('englishName')
                CONsempleItemProduct['description'] = item.get('englishDescription')
                CONsempleItemProduct['comment'] = item_comment
                CONsempleItemProduct['categoryName'] = item_categoryName
                CONsempleItemProduct['variation']['name'] = item.get('englishName')
                CONsempleItemProduct['unitPrice'] = str(item.get('price'))
                CONsempleItemProduct['paidPrice'] = item_paidPrice
                CONsempleItemProduct['discountAmount'] = item_discountAmount
                CONsempleItemProduct['quantity'] = item_quanttity
                CONsempleItemProduct['halfHalf'] = item_halfHalf
                CONsempleItemProduct['vatPercentage'] = item_vatPercentage
                CONfigProductGenerated.append(CONsempleItemProduct)
                #print(json.dumps(CONsempleItemProduct))

            elif "|T:CON".lower() in item.get('id').lower():
                CONcount=CONcount+1
                print("CON",CONcount)
                if item.get('choiceCategories', []):
                    choice_category = item.get('choiceCategories')
                    # print(choice_category)
                    choices = choice_category[0]['choices']
                    for choice in choices:
                        if not choice.get('choiceCategories', []):
                            # selected item attribute modification*******************************
                            CONfigitem = copy.deepcopy(BaseProduct)
                            CONfigitem_id = str(hash(item['englishName'] + ''.join(item)))
                            CONfigitem['id'] = CONfigitem_id
                            CONfigitem['remoteCode'] = item.get('id')
                            CONfigitem['name'] = item.get('englishName')
                            CONfigitem['description'] = item.get('englishDescription')
                            CONfigitem['comment'] = item_comment
                            CONfigitem['categoryName'] = item_categoryName
                            CONfigitem['variation']['name'] = item.get('englishName')
                            CONfigitem['unitPrice'] = str(item.get('price'))
                            CONfigitem['paidPrice'] = item_paidPrice
                            CONfigitem['discountAmount'] = item_discountAmount
                            CONfigitem['quantity'] = item_quanttity
                            CONfigitem['halfHalf'] = item_halfHalf
                            CONfigitem['vatPercentage'] = item_vatPercentage
                            # selected choice attribute modification*******************************
                            CONfigchoice_id = str(hash(choice['englishName'] + ''.join(choice)))
                            CONfigchoice = copy.deepcopy(BaseProduct.get('selectedToppings')[0])
                            CONfigitem['selectedToppings'][0]['id'] = CONfigchoice_id
                            CONfigitem['selectedToppings'][0]['remoteCode'] = choice.get('id')
                            CONfigitem['selectedToppings'][0]['name'] = choice.get('englishName')
                            CONfigitem['selectedToppings'][0]['quantity'] = choice_quanttity
                            CONfigitem['selectedToppings'][0]['children'] = []
                            CONfigitem['selectedToppings'][0]['price'] = str(choice.get('price'))
                            CONfigitem['selectedToppings'][0]['type'] = Selected_Topping_Type
                            # Appending product i.e storing in Configproduct
                            CONfigProductGenerated.append(CONfigitem)
                        else:
                            Items_Not_Configured = 1
                            print("*******************************************8")
                            print("remaining item", choice)
                            print("*******************************************8")
            elif "|T:BDL".lower() in item.get('id').lower():
                BDLcount=BDLcount+1
                print(BDLcount)
                CONfigbundleItemProduct=copy.deepcopy(bundleItemProduct)
                CONfigbundleItemProduct['id']= str(hash(item['englishName'] + ''.join(item)))
                CONfigbundleItemProduct['remoteCode']= item.get('id')
                CONfigbundleItemProduct['name'] = item.get('englishName')
                CONfigbundleItemProduct['description'] = item.get('englishDescription')
                CONfigbundleItemProduct['comment'] = item_comment
                CONfigbundleItemProduct['categoryName'] = item_categoryName
                CONfigbundleItemProduct['variation']['name'] = item.get('englishName')
                CONfigbundleItemProduct['unitPrice'] = str(item.get('price'))
                CONfigbundleItemProduct['paidPrice'] = item_paidPrice
                CONfigbundleItemProduct['discountAmount'] = item_discountAmount
                CONfigbundleItemProduct['quantity'] = item_quanttity
                CONfigbundleItemProduct['halfHalf'] = item_halfHalf
                CONfigbundleItemProduct['vatPercentage'] = item_vatPercentage
                CONfigbundleItemProduct['selectedChoices']=[]
                CONfigbundleItemProduct['selectedToppings'] = []
                #******************************************************************
                for choices in item.get('choiceCategories'):
                    print(choices.get('englishName'))
                    CONfigbundleItemchoice = copy.deepcopy(bundleItemProduct.get('selectedToppings')[0])
                    choice = copy.deepcopy(CONfigbundleItemchoice)
                    CONfigchoice_id = str(hash(choice['name'] + ''.join(choice)))
                    CONfigbundleItemchoice['id'] = CONfigchoice_id
                    CONfigbundleItemchoice['remoteCode'] = choice.get('id')
                    CONfigbundleItemchoice['name'] = choice.get('name')
                    CONfigbundleItemchoice['quantity'] = choice_quanttity
                    CONfigbundleItemchoice['children'] = []
                    CONfigbundleItemchoice['price'] = str(choice.get('price'))
                    CONfigbundleItemchoice['type'] = Selected_Topping_Type
                    CONfigbundleItemProduct['selectedToppings'].append(CONfigbundleItemchoice)
                print(json.dumps(CONfigbundleItemProduct))
            elif "|T:BDG".lower() in item.get('id').lower():
                print(item)


with open(f'{category_name}_products.json', 'w', encoding='UTF-8') as f:
    json.dump(CONfigProductGenerated, f, ensure_ascii=False, indent=4)
if Items_Not_Configured == 1:
    with open('Items Not Configured.json', 'w', encoding='UTF-8') as f:
      json.dump(CONfigProductGenerated, f, ensure_ascii=False, indent=4)
