import math

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

lcm = math.lcm(num1, num2)
gcd = math.gcd(num1, num2)

print("\n")
print("=" * 30)
print("\n")
print(f"The LCM of {num1} and {num2} is {lcm}.")
print(f"The GCD of {num1} and {num2} is {gcd}.")
print("\n")
print("=" * 30)
print("\n")