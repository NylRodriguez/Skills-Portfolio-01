# A dictionary mapping each month (1-12) to a tuple containing the month's name and the number of days in that month
days_in_month = {
    1: ("January", 31),  # January has 31 days
    2: ("February", 28),  # February has 28 days (29 on leap years)
    3: ("March", 31),  # March has 31 days
    4: ("April", 30),  # April has 30 days
    5: ("May", 31),  # May has 31 days
    6: ("June", 30),  # June has 30 days
    7: ("July", 31),  # July has 31 days
    8: ("August", 31),  # August has 31 days
    9: ("September", 30),  # September has 30 days
    10: ("October", 31),  # October has 31 days
    11: ("November", 30),  # November has 30 days
    12: ("December", 31)  # December has 31 days
}

# Function to check if a given year is a leap year
def check_leap_year(year):
# A leap year is divisible by 4 but not divisible by 100, unless also divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True  # It's a leap year
    return False  # Not a leap year

# Ask the user to input a month number (1 to 12)
month_num = int(input("Wanna know how many days in a month? Enter the month in number form (1-12): "))

# Check if the month number is valid (between 1 and 12)
if month_num < 1 or month_num > 12:
    print("Enter a number between 1 and 12. C’mon, keep it simple.")  # Prompt if the input is invalid
else:
# Retrieve the month name and number of days from the dictionary based on the input
    month_name, days = days_in_month[month_num]
    
# If the user selected February, check if it's a leap year
    if month_name == "February":
        year_input = int(input("Could you enter the year?: "))  # Ask the user for the year to check leap year
        if check_leap_year(year_input):
            print(f"February {year_input} has 29 days. It's a leap year, clearly.")  # Leap year case
        else:
            print(f"February {year_input} has 28 days. It's not a leap year.")  # Non-leap year case
    else:
# For other months, simply print the number of days in that month
        print(f"Month {month_num} ({month_name}) has {days} days. Simple math, really.")
