# Create an empty dictionary to store user information
user_info = {}

# Prompt the user to input their name and store it in the 'name' key of the dictionary
user_info['name'] = input("What is your name? ")

# Prompt the user to input their hometown and store it in the 'hometown' key of the dictionary
user_info['hometown'] = input("Where is your hometown? ")

# Loop until the user enters a valid age (a digit)
while True:
# Prompt the user to input their age
    age = input("How old are you? ")
    
# Check if the input is a valid number (a string of digits)
    if age.isdigit():
# Convert the input to an integer and store it in the 'age' key of the dictionary
        user_info['age'] = int(age)
# Exit the loop since we got a valid age
        break  

    else:
# If the input is not a number, ask the user to try again
        print("Please enter a number.")

# Print out the collected user information in vertical format
print("\nUser Information:")
# Print the user's name stored in the dictionary
print("Name: " + user_info['name'])
# Print the user's hometown stored in the dictionary
print("Hometown: " + user_info['hometown'])
# Print the user's age stored in the dictionary (convert the integer to a string for concatenation)
print("Age: " + str(user_info['age']))
