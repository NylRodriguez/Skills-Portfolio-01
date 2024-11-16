# Define the correct password
correct_code = "12345"

# Set the maximum number of attempts the user can make to enter the correct password
max_tries = 5

# Initialize the number of remaining tries to the maximum number of allowed attempts
remaining_tries = max_tries

# Start a loop that continues as long as there are remaining attempts
while remaining_tries > 0:
# Prompt the user to enter the password, showing how many attempts are left
    user_input = input(f"Enter the Password (Remaining tries: {remaining_tries}): ")

# Check if the entered password matches the correct password
    if user_input == correct_code:
        print("You're in!")  # If the password is correct, print a success message
        break  # Exit the loop since the user has successfully entered the correct password
    else:
# If the entered password is incorrect, reduce the number of remaining attempts by 1
        remaining_tries -= 1
        
# If there are still attempts left, encourage the user to try again
        if remaining_tries > 0:
            print(f"Let's keep it straight. {remaining_tries} tries left.")
        else:
# If there are no attempts left, print a final warning message
            print("Run for your life. Authorities have been notified.")
