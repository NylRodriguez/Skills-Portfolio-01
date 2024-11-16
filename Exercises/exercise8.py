# Define a list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Prompt the user to enter a name to search for in the list
specified_name = input("Enter the name you want to search for: ")

# Check if the entered name is in the 'names' list
if specified_name in names:
# If the name is found in the list, print a success message
    print(f"{specified_name} was found in the list!")
else:
# If the name is not found in the list, print a failure message
    print(f"{specified_name} was not found in the list.")


