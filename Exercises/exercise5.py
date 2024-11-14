days_in_month = {
    1: ("January", 31),
    2: ("February", 28),
    3: ("March", 31),
    4: ("April", 30),
    5: ("May", 31),
    6: ("June", 30),
    7: ("July", 31),
    8: ("August", 31),
    9: ("September", 30),
    10: ("October", 31),
    11: ("November", 30),
    12: ("December", 31)
}

def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

month_num = int(input("Wanna know how many days in a month? Enter the month in number form (1-12): "))

if month_num < 1 or month_num > 12:
    print("Enter a number between 1 and 12. C’mon, keep it simple.")
else:
    month_name, days = days_in_month[month_num] 
    if month_name == "February":
        year_input = int(input("Could you enter the year?: "))
        if check_leap_year(year_input):
            print(f"February {year_input} has 29 days. It's a leap year, clearly.")
        else:
            print(f"February {year_input} has 28 days. It's not a leap year.")
    else:
        print(f"Month {month_num} ({month_name}) has {days} days. Simple math, really.")


