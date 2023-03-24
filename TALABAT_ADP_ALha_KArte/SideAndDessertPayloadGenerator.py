import copy
import json

with open('sempleItem.json', encoding='UTF-8') as g:
    sempleItem = json.load(g)
with open('Sides & Desserts_products.json', 'r') as h:
    SideAndDessert = json.load(h)

ItemNotConfigured=0
ItemNotConfiguredprodeuct=[]
SideAndDessertPayload = []
Product_Price=0
printt=0

for product in SideAndDessert:
    CONfigsempleItem = copy.deepcopy(sempleItem)
    CONfigsempleItem['products']=[product]
    if not product.get("selectedToppings",[]):
        CONfigsempleItem['price']['subTotal'] = product.get('unitPrice')
        CONfigsempleItem['price']['totalNet'] = product.get('unitPrice')
        Deliveryfee=float(CONfigsempleItem['price']['deliveryFee'])
        CONfigsempleItem['price']['grandTotal'] =\
            str(float(product.get('unitPrice'))*int(product.get('quantity'))+Deliveryfee)
    if product.get('selectedToppings',[]):
        selectedToppings = product.get('selectedToppings')[0]
        if not selectedToppings.get("selectedToppings",[]):
            item_price=float(product.get('unitPrice'))
            price_selectedtopping=int(selectedToppings.get('quantity'))*float(selectedToppings.get('price'))
            Deliveryfee1 = float(CONfigsempleItem['price']['deliveryFee'])
            CONfigsempleItem['price']['subTotal'] = str(price_selectedtopping+item_price)*int(product.get('quantity'))
            CONfigsempleItem['price']['totalNet'] = str(price_selectedtopping+item_price)*int(product.get('quantity'))
            GrandTotal = str(Deliveryfee1+float(CONfigsempleItem['price'].get('totalNet')))
            CONfigsempleItem['price']['grandTotal']=GrandTotal
        if selectedToppings.get("selectedToppings",[]):
            ItemNotConfigured=1
            ItemNotConfiguredprodeuct.append(product)
    SideAndDessertPayload.append(CONfigsempleItem)
with open('Sides_And_Desserts_payload.json', 'w') as f:
    json.dump(SideAndDessertPayload, f, ensure_ascii=False, indent=4)
if ItemNotConfigured==1:
    with open('ItemNotConfiguredAtPriceLevel.json', 'w') as f:
        json.dump(ItemNotConfiguredprodeuct, f, ensure_ascii=False, indent=4)