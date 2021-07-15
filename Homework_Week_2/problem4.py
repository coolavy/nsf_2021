dollars = int(input("Enter the amount to change: "))

change = dollars // 2
change2 = dollars % 2


if change2 == 0:
    print(f"{change} two dollor bill(s) and 0 one dollar bill(s)")
else:
    print(f"{change} two dollar bill(s) 1 one dollar bill")