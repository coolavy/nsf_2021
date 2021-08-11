print("Welecome to the receipt generator!")
add_items = input("Do you want to add items (Y/n)?: ")

if add_items == "n":
    print("Thank you for using this program.")
else:
    
# These will be used later.
    item_details = []
    total = 0
    items_total = 0
    sub_total = 0
    tax = 0
    items_for_list = []
    line_lenght = 60

# Code for items, in the format (item : code)
    item_code = {
        "BRE" : "Bread",
        "MLK" : "Milk",
        "PIE" : "Pie"
    }

# Code for the price, in the format (item : price)
    item_price = {
        "BRE" : 2.00,
        "MLK" : 3.00,
        "PIE" : 3.14
    }

# If they need help with the item codes . . .
    print("For this format, please use a three letter code for each item. If you need theese codes, please enter 'y' or 'Y' below.")

    item_help = input("Do you need help (Y/n): ")
    
    if item_help == "n":
        print("You do not need any help")
    else:
        print("(Bread = BRE), (Milk = MLK), (Pie = PIE)")

    while True:
        
        enter_code = input("Enter list item code 1: ")
        if enter_code not in item_code:
            print(f"('{enter_code}') is not a vaild input.")
            continue
        print(f"{item_code[enter_code]} at $  {item_price[enter_code]}")
        
        quantity        = input("Enter list item quantity: ")
        add_more_items  = input("Do you want to add more items (Y/n)? : ")
        
        items_for_list.append((item_code[enter_code], quantity, item_price[enter_code]))
        
        sub_total    = sub_total + item_price[enter_code] * float(quantity)        
        items_total  = items_total + (item_price[enter_code] * int(quantity))
        
        product_name = item_code[enter_code]
        item_details.append(f"{'{:<35}'.format(product_name)}{quantity} @ $ {item_price[enter_code]:.2f} = $ {float(quantity) * float(item_price[enter_code]):.2f}")
        
        if add_more_items.lower() == "n":
            break 


    if add_more_items.lower() == "n":
        tax = sub_total * 0.05
        total = sub_total + tax
        print(f"List of items = {items_for_list}")
        print("Tax is 0.05% of the subtotal.")
        print("=" * line_lenght)
        print("R E C E I P T".center(line_lenght))
        print("=" * line_lenght)
        for item_detail in item_details:
            print(item_detail)
        print("-" * 60)
        print(f"{'{:<45}'.format('Sub total:')} $  {sub_total:.2f}")
        print(f"{'{:<36}'.format('Tax:')} @ 0.05% = $  {sub_total * 0.05:.2f}")
        print("-" * 60)
        print(f"{'{:<46}'.format('Total:')} $  {total:.2f}")