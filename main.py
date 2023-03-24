# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    import json

    # Open the JSON file for reading
    with open('C:\\Users\\anam.kumar\\PycharmProjects\\First\\TEST.json', encoding='UTF-8') as f:
        # Load the JSON data into a string

        y = json.load(f)
        data_str = json.dumps(y)

    # Print the JSON data as a string
    print(type(data_str))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
