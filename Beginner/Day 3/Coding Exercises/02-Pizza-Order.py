print('Welcome to the Python Pizza Deliveries!\n')

print('Price Table')
print('Small pizza: $15')
print('Medium pizza: $20')
print('Large pizza: $25\n')

print('Pepperoni for small pizza: +$2')
print('Pepperoni for Medium or Large pizza: +$3')
print('Extra cheese for any size pizza: +$1')
print('-----------------------------------------\n')

size = input('What size pizza do you want? S, M, or L? ').upper()
add_pepperoni = input('Do you want pepperoni? Y or N? ').upper()
extra_cheese = input('Do you want extra cheese? Y or N? ').upper()
bill = 0

if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
else:
    bill += 25
print(f'\nPizza Size {size}: ${bill}')

if add_pepperoni == 'Y' and size == 'S':
    bill += 2
    print(f'Pepperoni: $2')
elif add_pepperoni == 'Y':
    bill += 3
    print(f'Pepperoni: $3')

if extra_cheese == 'Y':
    bill += 1
    print(f'Extra Cheese: $1')

print(f'\nYour final bill is: ${bill}')
