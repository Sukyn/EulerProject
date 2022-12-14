'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''

if __name__ == '__main__':
    k = 10001
    primes = []
    i = 2
    while len(primes) < k:
        if all(i%prime != 0 for prime in primes):
            primes.append(i)
        i += 1
    result = primes[-1]
    print(result)
