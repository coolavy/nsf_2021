numbers = input("Enter a list of numbers, seperated by comma: ")

list = []

numbers = numbers.strip()

if numbers == "":
    print("Empty list.")
else:
    numbers = numbers.split(',')

    for (idx,el) in enumerate(numbers):
        b = int(el)
        list.append(b)
    
    print(f"int_list = {list}")

    list.sort()

    print(f"The largest element is {list[-1]}.")