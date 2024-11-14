user_info = {}

user_info['name'] = input("What is your name? ")
user_info['hometown'] = input("Where is your hometown? ")

while True:
    age = input("How old are you? ")
    if age.isdigit():
        user_info['age'] = int(age)
        break
    else:
        print("Please enter a number.")

print("\nUser Information:")
print("Name: " + user_info['name'])
print("Hometown: " + user_info['hometown'])
print("Age: " + str(user_info['age']))
