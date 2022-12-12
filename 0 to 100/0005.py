'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def decomp_prime(n):
    res = {}
    i = 1
    while i*i <= n:
        i += 1
        if n%i == 0:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
            n = int(n/i)
            i = 1

    if n in res:
        res[n] += 1
    else:
        res[n] = 1
    return res


def smallest_nb(k):
    res = 1
    for i in range(1, k+1):
        primes = decomp_prime(i)
        for factor in primes.keys():
            for j in range(0, primes[factor]):
                if res%(factor**primes[factor]) != 0:
                    res *= factor
    return res

if __name__ == '__main__':
    result = smallest_nb(20)
    print(result)
