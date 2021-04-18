from random import randint

row1 = ['⬜', '⬜', '⬜']
row2 = ['⬜', '⬜', '⬜']
row3 = ['⬜', '⬜', '⬜']

treasure_map = [row1, row2, row3]

print('\nX/Y   1       2        3')
print('1    ⬜      ⬜       ⬜')
print('2    ⬜      ⬜       ⬜')
print('3    ⬜      ⬜       ⬜')

random_value1 = randint(0, 2)
random_value2 = randint(0, 2)
treasure_map[random_value1][random_value2] = '✅'

position = input(
    '\nEnter Column followed by Row. eg: XY \nWhich spot do you want to mark? \n')

col = int(position[1]) - 1
row = int(position[0]) - 1

if col == random_value1 and row == random_value2:
    treasure_map[col][row] = '✅'
    status = True
else:
    treasure_map[col][row] = '💣'
    status = False

print('\n')
print(row1)
print(row2)
print(row3)

if status:
    print('\nYeah!, You located the Treasure🏴‍☠️.')
else:
    print('\nBooom!💣, You choose a wrong location,')
