

def get_primes(k):
    ''' Naive version
    Complexity : O(k)
    '''
    primes = [True]*(k+1)
    primes[0] = False
    primes[1] = False
    i = 2
    result = 0
    while i*i <= k:
        if primes[i]:
            for p in range(i*2, k+1, i):
                primes[p] = False
        i += 1

    for pos in range(k):
        if primes[pos]:
            result += pos
    return [i for i, val in enumerate(primes) if val]

if __name__ == '__main__':
    primes = get_primes(1000)

    len_max_primes = 0
    best_pair = (0, 0)
    for b in primes:
        for a in range(-1000, 1000):
            len_primes = 0
            i = 0
            while (i*i + i*a + b in primes):
                i += 1
                len_primes += 1
            #print("a=", a, "b=", b, "len=", len_primes, "maxlen=", len_max_primes, "bestpair=", best_pair)
            if len_primes > len_max_primes:
                len_max_primes = len_primes
                best_pair = (a, b)
    result = best_pair[0]*best_pair[1]
    print(result)
