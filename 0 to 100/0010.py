
'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
import time
import numpy as np

def get_prime_sum(k):
    ''' Naive version
    Complexity : O(k)*Time to check all modulos, really long
    '''
    primes = []
    i = 2
    result = 0
    for i in range(2, k):
        if all(prime >= np.sqrt(i) or i%prime != 0 for prime in primes):
            primes.append(i)
            result += i
    return result

def get_prime_sum_store(k):
    ''' Naive version
    Complexity : O(k)
    '''
    primes = [True]*(k+1)
    primes[1] = False
    i = 2
    result = 0
    while i*i <= k:
        if primes[i]:
            for p in range(i*2, k, i):
                primes[p] = False
        i += 1

    for pos in range(k):
        if primes[pos]:
            result += pos
    return result

if __name__ == '__main__':
    startTime = time.time()
    result = get_prime_sum(2000000)
    print(result, " in s:", time.time()-startTime)
    startTime = time.time()
    result = get_prime_sum_store(2000000)
    print(result, " in s:", time.time()-startTime)
