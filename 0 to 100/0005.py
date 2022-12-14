'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def decomp_prime(number):
    ''' Creates a dictionary which associates
    each prime number with its exposant in the prime
    decomposition of the number'''
    primes = {}
    i = 1
    while i*i <= number:
        i += 1
        if number%i == 0:
            if i in primes:
                primes[i] += 1
            else:
                primes[i] = 1
            number = number//i
            i = 1
    if number in primes:
        primes[number] += 1
    else:
        primes[number] = 1
    return primes


def smallest_nb(k):
    res = 1
    for i in range(1, k+1):
        primes = decomp_prime(i)
        for factor in primes.keys():
            for j in range(primes[factor]):
                if res%(factor**primes[factor]) != 0:
                    res *= factor
    return res

if __name__ == '__main__':
    result = smallest_nb(20)
    print(result)
