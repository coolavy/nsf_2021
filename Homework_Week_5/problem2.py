# Dicitonaries for the student, grade, and supples they need to buy.

# [

# Dicitonary for the student and their grade.
student_and_grade = {
    "jack" : "Third Grade",
    "jill" : "Fourth Grade"
}

# Dicitonary for the student and their supply list.
grade_supply_dict = {
    "Third Grade" : {'pen', 'pencil'},
    "Fourth Grade" : {'pen', 'maker', 'paper'}
}

# ]

# Inputs for the name of the student and the supplies the student has.
name = input("Enter student name: ")


# Formating the inputs
name = name.lower()


# If the student is forgein.
if name not in student_and_grade:
    print("Unknown student!")
#   Everything else . . .
else:
    student_supply_list = input("Items owned (separated by comma.): ")
    student_supply_list = student_supply_list.split(',')
    student_supply_set = set(student_supply_list)

    grade = student_and_grade[name]
    grade_supply_set = grade_supply_dict[grade]
    print("\n")
    print("=" * 50)
    print("\n")
    print(f"{name.title()} is in {grade}.")
    print(f"Items owned: {student_supply_set}")
    print(f"Items needed: {grade_supply_set}")

    print(f"Items needed for {grade}: {grade_supply_set}")

    missing_supplies = grade_supply_set - student_supply_set
    extra_supplies = student_supply_set - grade_supply_set

    print("\n")
    print("=" * 50)
    print("\n")
    print(f"Items owned and needed: {list(student_supply_set.intersection(grade_supply_set))}")
    if missing_supplies:
        print(f"Items needed but missing: {missing_supplies}")
    else:
        print("You have all your supplies (maybe some extra supplies) needed for your grade.")
    if not extra_supplies:
        print("You have no extra items.")
    else:
        print(f"Items owned but not needed: {extra_supplies}")
    print("\n")
    print("=" * 50)
    print("*" * 50)
    print("\n")
    print("Thank you for using this program. We really apeciate it.")
    print("\n")
    print("*" * 50)
    print("=" * 50)
            #       !!!!ALL DONE!!!!        #