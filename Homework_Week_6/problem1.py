def fib(x):
    sequence = [0,1]
    for n in range(x):
        sequence.append(sequence[-1] + sequence[-2])
    # print(sequence)
    return sequence[x]
x = int(input("Enter n: "))

result = fib(x)
print(f"fib({x}) is {result}")