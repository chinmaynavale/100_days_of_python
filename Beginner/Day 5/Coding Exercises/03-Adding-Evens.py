sum_of_evens = 0

# Method -1
for number in range(2, 101, 2):
    sum_of_evens += number

# Method -2
# for number in range(1, 101):
#     if number % 2 == 0:
#         sum_of_evens += number


print(f'sum of even numbers: {sum_of_evens}')
