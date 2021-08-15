def speed_category2(road_type, speed):
    highway_limit = 70
    city_limit = 30

    s_c = ""
    speed_limit = 0
    
    if road_type == "Highway":
        speed_limit = highway_limit
    if road_type == "City":
        speed_limit = city_limit

    if speed_limit * 0.80 > speed:
        s_c = "Slow"
    elif speed_limit * 0.80 < speed and speed_limit * 1.00 >= speed:
        s_c = "Right Speed"
    elif speed_limit * 1.00 < speed and speed_limit * 1.05 >= speed:
        s_c = "Slightly Fast"
    else:
        s_c = "Very Fast"
    return s_c


road_type = str(input("Road Type: "))
road_type = road_type.title()
if road_type not in ["City", "Highway"]:
    print("Invaild Road Type.")
else:
    speed = int(input("Speed: "))

    s_c = speed_category2(road_type, speed)

    print(f"Road Type: {road_type}, Speed: {speed} - Result: {s_c}")