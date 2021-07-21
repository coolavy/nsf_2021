a = int(input("Enter the first side of the triangle: "))
b = int(input("Enter the second side of the triangle: "))
c = int(input("Enter the third side of the triangle: "))

if a == b == c:
    print("This triangle is an Equilateral Triangle")

elif a == b or b == c or a == c:
    print("This triangle is an Isosceles Triangle")
else:
    print("This triangle is a Scalene Triangle")