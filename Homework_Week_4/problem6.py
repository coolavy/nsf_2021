numbers = input("Enter a list of numbers, seperated by comma: ")

list = []

numbers = numbers.strip()

if numbers == "":
    print("Empty List.")
else:
    numbers = numbers.split(',')
    for (idx,el) in enumerate(numbers):
        b = int(el)
        list.append(b)
    
    print(f"int_list = {list}")
    list.sort()
    print(f"Smallest element is {list[0]}")
    print(f"Largest element is {list[-1]}")
    print(f"Sum of all the elements is {sum(list)}")
    if len(list) == 1:
        print(f"Partial Sum: 0")
    else:
        print(f"Partial Sum: {sum(list) - list[0] - list[-1]}")
