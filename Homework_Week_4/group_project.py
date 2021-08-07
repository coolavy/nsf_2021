print("Welecome to the receipt generator!")
add_items = input("Do you want to add items (Y/n)?: ")

if add_items == "n":
    print("Thank you for using this program.")

item_details = []
items_total = 0
sub_total = 0
tax = 0

while add_items == "y":
    ## inputs
    name        = input(f"Enter item name {items_total + 1}: ")
    quantity    = int(input(f"Enter item quantity {items_total + 1}: "))
    price       = float(input(f"Enter list item price {items_total + 1}: "))
    
    ## running subtotal
    sub_total = sub_total + price * quantity
    items_total = items_total + 1
    
    name = name.title()
    
    ## add items details for receipt
    item_details.append(f"{'{:<20}'.format(name)}{quantity} @ $  {price:.2f} = $  {quantity * price:.2f}")
    add_more_items = input("Do you want to add more items (Y/n)?: ")
    
    if add_more_items == "n":
        print("=" * 45)
        print("R E C E I P T".center(45))
        print("=" * 45)
        
        for item_detail in item_details:
            print(item_detail)
        print("-" * 45)
        
        print(f"Sub total:{'{:>25}'.format('$')}  {sub_total:.2f}")
        tax = sub_total * 0.05
        
        print(f"Tax:{'{:>33}'.format('@ 0.05 = ')}{tax:.2f}")
        print("-" * 45)
        
        total = "{:.2f}".format(sub_total + tax)
        print(f"Total:{'{:>35}'.format('$' + total)}")
        break