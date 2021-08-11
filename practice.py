# fruit = {
#     "oranges": 1.49,
#     "apples": 1.28,
#     "bananas": 0.49,
#     "papayas": 3.99,
#     "pears": 0.88
# }

# fruit_quantity = {
#     "oranges": 12,
#     "apples": 5,
#     "bananas": 24,
#     "papayas": 5,
#     "pears": 8
# }

# total = 0

# for key,price in fruit.items():
#     total = total + fruit_quantity[key] * price

# print(total.__round__())

# apple_price = fruit["apples"] * fruit_quantity["apples"]

# print(apple_price.__round__())

# n = int(input("Enter a number: "))


# def number():
#     absulote = n - n * 2
#     print(f"The absulote of {n} is {absulote}.")

number = int(input("Enter a number: "))

if number < 0:
    print(f"{number} is negitave.")
elif number > 0:
    print(f"{number} is positive.")
else:
    print(f"{number} is 0.")