import time
def fib(x):
    sequence = [0,1]
    for n in range(x):
        sequence.append(sequence[-1] + sequence[-2])
    # print(sequence)
    return sequence[x]
x = int(input("Enter n: "))
t0 = time.time()

result = fib(x)
t1 = time.time()
print(f"fib({x}) is {result}")
result = str(result)
print(f"{result} is {len(result)} digits long.")
print(f"It took {t1 - t0:.15f}")