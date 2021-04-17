print('Welcome to Treasure Island.')
print('Your mission is to find the trasure.\n')

choice1 = input(
    'You\'re at a cross road, Where do you want to go? Type "Left" or "Right"\n').lower()

if choice1 == 'left':
    choice2 = input(
        'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if choice2 == 'wait':
        choice3 = input(
            'You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n').lower()
        if choice3 == 'yellow':
            print('You found the 🏴‍☠️ Treasure🏴‍☠️. You Win.')
        elif choice3 == 'red':
            print('It\'s a room full of 🔥Fire🔥. Game Over.')
        elif choice3 == 'blue':
            print('You enter a room full of 🦉Bats🦉. Game Over.')
        else:
            print('You choose a room that doesn\'t exist')
    else:
        print('You got attacked by an angry 👿Trout👿. Game Over.')
else:
    print('You fell into a hole🕳. Game Over.')
