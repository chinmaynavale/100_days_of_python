from random import choice
from hangman_words import word_list
from hangman_art import logo, stages

choosen_word = choice(word_list)
guessed_word = ['_' for each in choosen_word]

print(logo)
print(f'You have 7 lives to guess the word : {" ".join(guessed_word)}\n')

lives = 7
while lives:
    guess = input('\nGuess a letter: ')

    if guess in guessed_word:
        print('You have already made this guess before! Try a new guess.\n')
    elif guess in choosen_word:
        index = 0
        for letter in choosen_word:
            if letter == guess:
                guessed_word[index] = guess
            index += 1
        print(f'{" ".join(guessed_word)}\n')
    else:
        lives -= 1
        print(f'{stages[lives]}\nWrong Guess, Lives remaining: {lives}')

    if '_' not in guessed_word:
        print('\n\nYou won! You guessed it all.')
        break
else:
    print(f'\n\nGame Over\nThe Word was "{choosen_word}"')
