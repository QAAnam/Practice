import json
with open('C:\\Users\\anam.kumar\\PycharmProjects\\First\\Experimented.json', encoding='UTF-8') as f:
    # Load the JSON data into a Python dictionary
    nested_json1 = json.load(f)
nested_json={
    "id": "123",
    "name": "Example",
    "items": [
        {
            "id": "456",
            "name": "Item 1",
            "choiceCategories": []
        },
        {
            "id": "789",
            "name": "Item 2",
            "choiceCategories": [
                {
                    "id": "111",
                    "name": "Category 1",
                    "options": [
                        {
                            "id": "222",
                            "name": "Option 1",
                            "choiceCategories": []
                        }
                    ]
                }
            ]
        },
        {
            "id": "321",
            "name": "Item 3",
            "choiceCategories": []
        }
    ]
}
def find_dict_with_empty_choiceCategories(nested_dict):
    if isinstance(nested_dict, dict):
        if nested_dict.get("choiceCategories") == []:
            print(nested_dict)
        for value in nested_dict.values():
            find_dict_with_empty_choiceCategories(value)
    elif isinstance(nested_dict, list):
        for item in nested_dict:
            find_dict_with_empty_choiceCategories(item)
find_dict_with_empty_choiceCategories(nested_json1)

#find_dict_with_empty_choiceCategories(nested_json1)
