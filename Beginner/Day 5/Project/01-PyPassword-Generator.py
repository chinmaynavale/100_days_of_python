from random import choice
from string import ascii_letters, punctuation, digits
from random import shuffle

print('Welcome to the PyPassword Generator!')

no_of_letters = int(
    input('How many letters would you like in your password? '))
no_of_symbols = int(input('How many symbols would you like? '))
no_of_numbers = int(input('How many numbers would you like? '))


letters = [choice(ascii_letters) for i in range(no_of_letters)]
symbols = [choice(punctuation) for i in range(no_of_symbols)]
numbers = [choice(digits) for i in range(no_of_numbers)]

password = letters + symbols + numbers
easy_password = ''.join(password)
shuffle(password)
password = ''.join(password)

print(f'The easy password is: {easy_password}')
print(f'The hard password is: {password}')
