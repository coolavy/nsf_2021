print('Hello! Please enter your time.')
hours = int(input("Please enter the number of hours that passed: "))
minutes = int(input("Please enter the number of minutes that passed: "))

time_in_minutes = hours * 60 + minutes

print(f"{hours} hours and {minutes} minutes is {time_in_minutes} minutes.")