number_of_items = int(input("Enter number of items: "))
item_details = []
items_total = 0
for index in range(0, number_of_items):

    # inputs

    name = input(f"Enter item{index + 1} name: ")
    price = float(input(f"Enter item{index + 1} price: "))
    quantity = int(input(f"Enter item{index + 1} quantity: "))

    print("\n")
    # total

    total = quantity * price
    items_total = items_total + total
    item_details.append(f"{quantity} {name} @ ${price:.2f} = ${total:.2f}")

# Printing Receipet

print("RECIEPT")

for item_detail in item_details:
    print(item_detail)

print(f"Total cost: ${items_total:.2f}")

# add empty line
print("\n")

tax = items_total * 0.05

print(f"5% tax: ${tax:.2f}")
print(f"Total with tax: ${items_total + tax:.2f}")