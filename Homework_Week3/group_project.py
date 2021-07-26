print("Welecome to highway search protal!")

highway_number = 1 

while highway_number > 0:
    highway_number = int(input("Please enter a number (0 to quit): "))
    if highway_number == 0:
        print("Thank you for using the highway search prtal.")
        print("Have a great day!")
        break
    elif highway_number in range(1, 100) and highway_number % 2 == 0:
        print(f"Highway {highway_number} is a main highway, going east/west.")
    elif highway_number in range(1, 100) and highway_number % 2 == 1:
        print(f"Highway {highway_number} is a main highway, going north/south.")
    elif highway_number in range(100, 1000) and (highway_number % 100) % 2 == 0:
        print(f"Highway {highway_number} is an auxiliary highway serving primary highway {highway_number % 100}, going east/west.")
    else:
        print(f"Highway {highway_number} is an axuiliary highway serving primary highway {highway_number % 100}, going north/south.")


