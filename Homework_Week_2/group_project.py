# inputs

name = input("Enter item name: ")
price = float(input("Enter item price: "))
quantity = int(input("Enter item quantity: "))

# total

total = quantity * price 

# Printing Receipet

print(f'''
RECEIPT
{quantity} {name} @ ${price} = ${total}
Total cost: ${total}''')

# a and b are done
# To Do = c and d