from random import randint

names_string = input('Give me everybody\'s name seperated by a comma. ')
names = names_string.split(', ')

bill_payer = names[randint(0, len(names)-1)].capitalize()
print(f'{bill_payer} is going to buy the meal today!')
