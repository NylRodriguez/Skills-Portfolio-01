# A dictionary that maps country names to their capitals
country_capital_map = { 
    'France': 'Paris',  # Capital of France
    'Germany': 'Berlin',  # Capital of Germany
    'Italy': 'Rome',  # Capital of Italy
    'Spain': 'Madrid',  # Capital of Spain
    'United Kingdom': 'London',  # Capital of the United Kingdom
    'Luxembourg': 'Luxembourg City',  # Capital of Luxembourg
    'Liechtenstein': 'Vaduz',  # Capital of Liechtenstein
    'Malta': 'Valletta',  # Capital of Malta
    'San Marino': 'City of San Marino',  # Capital of San Marino
    'Andorra': 'Andorra la Vella'  # Capital of Andorra
}

# Initialize the score counter to 0
score = 0

# Loop through each country and its corresponding capital in the dictionary
for nation, correct_capital in country_capital_map.items():
    # Prompt the user to input the capital for the current country
    user_input = input(f"The Capital of {nation} is? ").strip()
    
# Check if the user input matches the correct capital, case-insensitively
    if user_input.lower() == correct_capital.lower():
        print("Next!")  # If the answer is correct, move on
        score += 1  # Increment the score for a correct answer
    else:
        print(f"Don't you think it's {correct_capital}?")  # If the answer is wrong, suggest the correct capital

# After the loop, print the user's final score out of 10
print(f"\n {score} out of 10.")

# Provide feedback based on the user's score
if score == 10:
    print("It's either you are the top on your geo class or you travel a lot!")
elif score >= 8:
    print("Not too shabby")
elif score >= 6:
    print("Congrats on being above average...I guess?")
elif score >= 4:
    print("I Guess somebody is not listening on their geo class")
elif score >= 2:
    print("You're cooked bro...")
else:
    print("Maybe the countries I encoded are not popular :P")
