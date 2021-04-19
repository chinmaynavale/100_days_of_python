from random import randint


def temp():
    if players_choice == rock:
        print(f'{rock_symbol}  \n\nComputer choose')
        if computers_choice == paper:
            print('You Loose!')
        elif computers_choice == scissors:
            print('You Win!')
        else:
            print('Its a Draw.')

    elif players_choice == paper:
        print(f'{paper_symbol}  \n\nComputer choose')
        if computers_choice == rock:
            print('You Win!')
        elif computers_choice == scissors:
            print('You Loose!')
        else:
            print('Its a Draw.')

    elif players_choice == scissors:
        print(f'{scissors_symbol}  \n\nComputer choose')
        if computers_choice == rock:
            print('You Loose!')
        elif computers_choice == paper:
            print('You Win!')
        else:
            print('Its a Draw.')
    else:
        print('Wrong Input, Please Try Again!')


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input(
    'Choices \n 0 => Rock,\n 1 => Paper,\n 2 => Scissors.\nWhat do you choose?  '))

if user_choice >= 3 or user_choice < 0:
    print('You choose a wrong input, You Lose!')
else:
    print(game_images[user_choice])

    computers_choice = randint(0, 2)
    print(f'Computer choose: \n {game_images[computers_choice]}')

    rock, paper, scissors = 0, 1, 2

    if user_choice == computers_choice:
        print('Its a Draw')
    elif user_choice == 0 and computers_choice == 2:
        print('You Win!')
    elif user_choice == 2 and computers_choice == 0:
        print('You Lose!')
    elif computers_choice > user_choice:
        print('You Lose!')
    elif user_choice > computers_choice:
        print('You Win!')
