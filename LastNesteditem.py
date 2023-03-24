import json

# example nested JSON
nested_json = {
    "id": "123",
    "name": "Example",
    "items": [
        {
            "id": "456",
            "name": "Item 1",
            "choiceCategories": None
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
                            "choiceCategories": None
                        }
                    ]
                }
            ]
        },
        {
            "id": "321",
            "name": "Item 3",
            "choiceCategories": None
        }
    ]
}

# function to recursively print items with null choiceCategories
def print_items_with_null_choice_categories(nested_json):
    if isinstance(nested_json, list):
        for item in nested_json:
            print_items_with_null_choice_categories(item)
    elif isinstance(nested_json, dict):
        if "choiceCategories" in nested_json and nested_json["choiceCategories"] is None:
            print(nested_json["name"])
        for value in nested_json.values():
            print_items_with_null_choice_categories(value)

# calling the function
print_items_with_null_choice_categories(nested_json)
