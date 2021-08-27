item_code = {}
item_price = {}

def add_new_product(product_code, product_name, product_price):
    item_code[product_code] = product_name
    item_price[product_code] = product_price

def print_receipt(sub_total, items_for_list, item_details, line_lenght):
    base_tax = 5.00
    tax = sub_total * (base_tax / 100)
    total = sub_total + tax
    print(f"List of items = {items_for_list}")
    print(f"Tax is {base_tax}% of the subtotal.")
    print("=" * line_lenght)
    print("R E C E I P T".center(line_lenght))
    print("=" * line_lenght)
    for item_detail in item_details:
        print(item_detail)
    print("-" * line_lenght)
    print(f"{'{:<45}'.format('Sub total:')} $  {sub_total:.2f}")
    print(f"{'{:<36}'.format('Tax:')} @ 0.05% = $  {sub_total * 0.05:.2f}")
    print("-" * line_lenght)
    print(f"{'{:<45}'.format('Total:')} $  {total:.2f}")
    print("=" * line_lenght)

def initialize():
    file_path = "nsf_2021\Homework_Week_7\problems\pricelist.txt"
    opening_file = open(file_path, "r")
    for line in opening_file:
        line = line.strip()
        line = line.split(',')
        print(line)
        add_new_product(line[0], line[1], float(line[2]))
    print(item_code)
    print(item_price)
    opening_file.close()

def accept_input():
        # Variables     
    item_details = []
    items_total = 0
    sub_total = 0
    items_for_list = []

    while True:
        enter_code1 = input("Enter list item code 1: ")
        enter_code = enter_code1.title()
        if enter_code not in item_code:
            print(f"Code ({enter_code1}) is not found.")
            new_product_name = input(f"Enter name for {enter_code1}: ")
            new_product_price = float(input(f"Enter price for {enter_code1}: "))
            add_new_product(enter_code, new_product_name, new_product_price)

        
        print(f"{item_code[enter_code]} at $  {item_price[enter_code]:.2f}")
        quantity        = input("Enter list item quantity: ")
        add_more_items  = input("Do you want to add more items (Y/n)? : ")
        
        items_for_list.append((item_code[enter_code], quantity, item_price[enter_code]))
        
        sub_total    = sub_total + item_price[enter_code] * float(quantity)        
        items_total  = items_total + (item_price[enter_code] * int(quantity))
        
        product_name = item_code[enter_code]
        item_details.append(f"{'{:<35}'.format(product_name)}{quantity} @ $ {item_price[enter_code]:.2f} = $ {float(quantity) * float(item_price[enter_code]):.2f}")
        
        if add_more_items.lower() == "n":
            break
    return sub_total, items_for_list, item_details

def main():    
    print("Welecome to the receipt generator!")
    add_items = input("Do you want to add items (Y/n)?: ")

    if add_items == "n":
        print("Thank you for using this program. See you next time!")
    else:
        initialize()

        # Variables     
        line_lenght = 60

        sub_total, items_for_list, item_details = accept_input()
        print_receipt(sub_total, items_for_list, item_details, line_lenght)

if __name__ == "__main__":
    main()