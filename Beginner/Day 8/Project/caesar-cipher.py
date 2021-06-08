from string import ascii_lowercase
from art import logo
alphabet = list(ascii_lowercase)


def caeser(start_text, shift_amount, cipher_direction):
    end_text = ''

    if cipher_direction == 'decode':
        shift_amount *= -1

    for char in start_text:
        if char in alphabet:
            i = alphabet.index(char)
            end_text += alphabet[(i + shift_amount) % 26]
        else:
            end_text += char

    print(f'The {cipher_direction}d message is: {end_text} \n')


print(logo)
while True:
    direction = input('Type "encode" to encrypt, type "decode" to decrypt: \n')
    text = input('Type your message: \n').lower()
    shift = int(input('Type the shift number: \n'))

    caeser(text, shift, direction)

    result = input(
        'Do you wish to continue? "yes" or "no":  ')
    if result.lower() == 'no':
        print('Goodbye')
        break
