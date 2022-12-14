'''


Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
import time
import numpy as np

divisors = {1: []}

def find_divisors(n):
    ''' Find all divisors of n '''
    tmp_divisors = [1]
    for i in range(2, int(np.sqrt(n)) + 1):
        if n%i == 0:
            tmp_divisors = [*set(tmp_divisors + [i] + [n//i])]
    divisors[n] = tmp_divisors
    return sum(tmp_divisors)

def find_amicable(k):
    ''' Find amicable pairs '''
    for i in range(k+1):
        find_divisors(i)

    result = 0
    for number in range(k+1//2):
        val = sum(divisors[number])
        if val <= k and sum(divisors[val]) == number and val < number:
            result += val + number
    return result

if __name__ == '__main__':
    startTime = time.time()
    result = find_amicable(100000)
    print(divisors)
    print(result, "in s:", time.time()-startTime)
