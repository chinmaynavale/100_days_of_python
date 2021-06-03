n = int(input('Check this number: '))


def prime_checker(num):
    isprime = True

    for each_num in range(2, num):
        if num % each_num == 0:
            isprime = False

    if isprime:
        print('It\'s a prime number.')
    else:
        print('It\'s not a prime number.')


prime_checker(n)
