fruit = {
    "oranges": 1.49,
    "apples": 1.28,
    "bananas": 0.49,
    "papayas": 3.99,
    "pears": 0.88
}

fruit_quantity = {
    "oranges": 12,
    "apples": 5,
    "bananas": 24,
    "papayas": 5,
    "pears": 8
}

total = 0

for key,price in fruit.items():
    total = total + fruit_quantity[key] * price

print(total.__round__())

apple_price = fruit["apples"] * fruit_quantity["apples"]

print(apple_price.__round__())