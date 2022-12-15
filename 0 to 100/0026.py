
import time

def cycle_length(n):
    a = 10 # Basic algorithm, started at first step
    b = n
    cpt = 0
    while (a != 10 or cpt <= 1):
        a = (a%b) * 10
        cpt +=1
    return cpt

def get_primes(k):
    ''' Generates all primes from 2 to k'''
    primes = [True]*(k+1)
    primes[0] = False
    primes[1] = False
    i = 2

    while i*i <= k:
        if primes[i]:
            for p in range(i*2, k+1, i): # Multiples of i
                primes[p] = False
        i += 1

    result = 0
    for pos in range(k):
        if primes[pos]:
            result += pos
    return [i for i, val in enumerate(primes) if val]


if __name__ == '__main__':
    startTime = time.time()
    result = 0
    max_len = 0
    max_val = 0
    primes = get_primes(1001)

    primes = primes[3:] # Remove 2 and 5 because there are no cycles
    for i in primes:
        c = cycle_length(i)
        if c > max_len:
            max_len = c
            max_val = i
    print(max_val, "in", time.time() - startTime)
