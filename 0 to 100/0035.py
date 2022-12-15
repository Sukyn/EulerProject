import time

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

primes = get_primes(1000000)

to_check = set(i for i in range(3, 1000000, 2) if not set(['2', '4', '6', '8', '0']) & set(str(i).strip()))
to_check.add(2)

def is_circular_prime(n):
    global primes
    if not n in primes:
        return False
    digits = list(map(int, str(n).strip()))
    for i in range(1, len(digits)):
        digits = digits[1:] + digits[:1]
        if int("".join(list(map(str,digits)))) not in primes:
            return False
    return True

if __name__ == '__main__':
    startTime = time.time()
    result = 0
    while len(to_check) > 0:
        i = to_check.pop()

        digits = list(map(int, str(i).strip()))

        val = is_circular_prime(i)

        if val:
            result += 1
            print(i, result)

        for j in range(1, len(digits)):
            digits = digits[1:] + [digits[0]]
            new_numb = int("".join(list(map(str,digits))))
            if new_numb in to_check:
                to_check.remove(new_numb)
            if val and new_numb != i:

                result += 1
                print(new_numb, result)

    print(result, "in", time.time() - startTime)
