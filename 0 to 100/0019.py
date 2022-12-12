'''


You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

'''

'''1 Jan 1900 was a Monday.'''
day = 1 # Base = 1 Jan 1900, Monday so 1

def is_leap_year(n):
    return n%4 == 0 and (n%100 != 0 or n%400 == 0)


if __name__ == '__main__':
    result = 0
    for year in range(1900, 2000+1):
        if is_leap_year(year):
            feb = 29
        else:
            feb = 28
        day_by_month = [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        for month in day_by_month:

            if year > 1900 and day == 0:
                result += 1

            day = (day+month)%7

    print(result)
