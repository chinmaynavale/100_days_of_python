def is_leap(year):
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0


def days_in_month(year, month):
    if month < 1 or month > 12:
        return 'Invalid Month'

    month_days = [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
    if month == 2 and is_leap(year):
        return 29
    return month_days[month-1]


year = int(input('Enter a year: '))
month = int(input('Enter a month[1-12]: '))
days = days_in_month(year, month)
print(days)
