'''

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
import numpy as np

divisors = {1: 0}

def find_divisors(n):
    ''' Find all divisors of n '''
    if n in divisors:
        return divisors[n]

    tmp_divisors = [1]
    for i in range(2, int(np.sqrt(n)) + 1):
        if n%i == 0:
            tmp_divisors = [*set(tmp_divisors + [i] + [n//i])]
    sumd = sum(tmp_divisors)
    divisors[n] = sumd
    return sumd

def is_abundant(n):
    return find_divisors(n) > n

def is_sum_of_abundant(n):
    for i in range(1, n//2 + 1):
        if is_abundant(i) and is_abundant(n-i):
            return True
    return False

if __name__ == '__main__':

    result = 0
    for i in range(28123):
        #print(divisors)
        if not is_sum_of_abundant(i):
            print(i)
            result += i
    print(result)
