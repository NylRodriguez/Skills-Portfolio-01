# Define a function that checks if a given age is even or odd
def age_even_odd(age):
# Check if the age is divisible by 2 (even number)
    if age % 2 == 0:
        return str(age) + " " + "is even"  # Return the message indicating the age is even
    else:
        return str(age) + " " + "is odd"  # Return the message indicating the age is odd

# Define the main function where the user input and logic will be handled
def main():
# Ask the user to input their age
    user_input = input("Please enter your age: ")

# Try to convert the user input into an integer
    try:
        number = int(user_input)  # Try to convert the input to an integer
        result = age_even_odd(number)  # Call the age_even_odd function to determine if the number is even or odd
        print(result)  # Print the result returned by the age_even_odd function
    except ValueError:
# If a ValueError occurs (e.g., the input can't be converted to an integer), print this message
        print("Make sure to enter a number.")  # Handle the case where the user didn't enter a valid number

# This block ensures that the main function is called only when the script is run directly
if __name__ == "__main__":  
    main()  # Call the main function to start the program



 
