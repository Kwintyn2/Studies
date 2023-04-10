from Supermarket_moduller import *

print("""Supermarket Item Adder
1. Item Search
2. Item Add
3. Item Counts Edit
4. Item Delete
5. All Items
Type "Exit" for exit the program
""")

reyons = reyons()

while True:
    usr_value = input("Please choose your process: ")
    if usr_value.lower() == "exit":
        print("Exiting the Program")
        time.sleep(1)
        break

    elif usr_value == "1":
        usr_value = input("Enter the item name you want to search: ")
        reyons.search_item(usr_value)

    elif usr_value == "2":
        name = input("Enter the item name: ")
        price = input("Enter the item's price: ")
        counts = input("Enter the item's count(s)")
        newitem = item(name, price, counts)
        reyons.new_item(newitem)

    elif usr_value == "3":
        item_name = input("Enter the item name you want to add to the count: ")
        if reyons.search_item(item_name):
            pass
        else:
            new_count = input("Enter the count you want to add to: ")
            reyons.increase_count(item_name, new_count)
    elif usr_value == "4":
        item_name = input("Enter the item name that you want to delete: ")
        if reyons.search_item(usr_value):
            decision = input("Are you sure you want to delete this item ? (Y/N) ")
            if decision == "Y":
                reyons.delete_item(item_name)

    elif usr_value == "5":
        reyons.all_items()

    else:
        print("Wrong input !")