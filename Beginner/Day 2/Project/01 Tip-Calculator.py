print('Welcome to the Tip Calculator.\n')

bill = float(input('What was the total bill? \n₹'))
percentage_tip = int(input(
    'What percentage tip would you like to give? 10, 12, or 15? \n'))
no_of_people = int(input('How many people to split the bill? \n'))

tip = bill * percentage_tip / 100
total_bill = bill + tip
bill_per_person = round(total_bill/no_of_people, 2)

print(f'\nEach person should pay: ₹{bill_per_person:.2f}')
