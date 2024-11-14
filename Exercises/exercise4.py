country_capital_map = { 
    'France': 'Paris',
    'Germany': 'Berlin',
    'Italy': 'Rome',
    'Spain': 'Madrid',
    'United Kingdom': 'London',
    'Luxembourg': 'Luxembourg City',
    'Liechtenstein': 'Vaduz',
    'Malta': 'Valletta',
    'San Marino': 'City of San Marino',
    'Andorra': 'Andorra la Vella'
}

score = 0

for nation, correct_capital in country_capital_map.items():
    user_input = input(f"The Capital of {nation} is? ").strip()
    
    if user_input.lower() == correct_capital.lower():
        print("Next!")
    else:
        print(f"Don't you think it's {correct_capital}?")

print(f"\n {score} out of 10.")

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