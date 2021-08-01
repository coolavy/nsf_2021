print("Welecome! This program is designed to give you a list of items. To end this program, type 'end'.")
add_items = input("Do you want to add items to the list (y/n): ")

add_items = add_items.lower()

index = 0

item_list = []
item_list2 = []
if add_items == "n":
    print("Thank you for using this program.")
else:
    while add_items == "y":
        if index != 0:
            add_items = input("Do you want to add items to the list (y/n): ")
            add_items = add_items.lower()
        index = index + 1
        if add_items == "y":
            item = input("Enter item: ")
            item_list.append(item)

            if item.strip() != "":
                item_list2.append(item)
        else:
            print(f"Input List = {item_list}")
            print(f"Output List is {item_list2}")
            print("Thank you for using this program.")
            break