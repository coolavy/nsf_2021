print("Hello, welecome to the fuel cost calculator.")

# questions to caluctor the mileage
# formula for mileage = miles / gallons             
# formula for total cost of fuel = gallons X cost/gallon     
# example = mileage = 750/25 = 30
# example = total cost = 25 X 3 = 75


# Questions to make decisions 

trip_distance = int(input("Please enter the trip distance in miles: "))
number_of_gallons = int(input("Please ente the number of gallons of fuel used: "))

# Formulas

mileage = trip_distance / number_of_gallons

# Answer for first Question

print(f"The mileage of the car is {mileage}.")

# Questions 

price_per_gallon = int(input("Please enter the price paid in dollars per gallon of fuel: "))

# Formulas

total_cost_of_fuel = number_of_gallons * price_per_gallon

# Final step

print(f"The total cost of fuel for the trip is: {total_cost_of_fuel}")