month = int(input("Enter the month as a number: "))
day = int(input("Enter the date: "))

if (month == 3 and day >= 20) or month in (4, 5) or (month == 6 and day < 20):
    print("It is spring.")
elif (month == 6 and day >= 20) or month in (7, 8) or (month == 9 and day < 22):
    print("It is summer")
elif (month == 9 and day >= 22) or month in (10, 11) or (month == 12 and day < 21):
    print("It is fall.")
elif (month == 12 and day >= 21) or month in (1, 2) or (month == 3 and day < 20):
    print("It is winter.")
else:
    print("Invaild month and/or date. ")