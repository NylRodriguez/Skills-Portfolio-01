names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

specified_name = input("Enter the name you want to search for: ")

if specified_name in names:
    print(f"{specified_name} was found in the list!")
else:
    print(f"{specified_name} was not found in the list.")

