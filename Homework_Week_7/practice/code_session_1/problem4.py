from datetime import date

def age_in_years(year, month, day):
    
    today = date.today()
    input_date = date(year, month, day)

    difference_in_days = today - input_date
    difference_in_days_number = difference_in_days.days
    difference_in_years = difference_in_days_number // 365

    print(f"You are {difference_in_years} old.")

year = int(input("Enter the year you were born: "))
month = int(input("Enter the moth you were born: "))
day = int(input("Enter the day you were born: "))

age_in_years(year, month, day)