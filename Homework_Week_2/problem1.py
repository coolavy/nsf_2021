print('Welecome! Please enter your time in 24 Hour format.')
hours = int(input("Please enter the number of hours that passed: "))
minutes = input("Please enter the number of minutes that passed: ")

if hours > 12:
    hours = hours - 12

print(f"The time is {hours}:{minutes} in 12 hour clock format.")