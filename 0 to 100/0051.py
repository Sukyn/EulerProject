'''

By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
'''
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


def unrank(s, i):
    ''' Generates all subsets of s
    (useful to check for multiple digits)'''
    if s == []: # If s is empty, [] is the only subset
        return []
    s0 = s.pop(0)
    if i >= 2**len(s):
        return [s0] + unrank(s, i-2**len(s))
    else:
        return unrank(s, i)

if __name__ == '__main__':

    startTime = time.time()
    primes = get_primes(1000000) # Let's pray the number is < 10000000
    max_len = 0
    lowest = 0 # Result value
    while max_len < 8:

        # Get the first unexplored prime
        p = primes.pop(0)

        # Separate digits
        digits = list(map(int, str(p).strip()))

        # pos will be the position of changing bits
        for pos in range(1, 2**len(digits)):

            # Generate the subcombination
            changing_pos = unrank([i for i in range(len(digits))], pos)

            # Check the value of the first modified digit
            fst_digit = digits[changing_pos[0]]

            # Check that every digit we want to modify are equal
            if all(digits[i] == fst_digit for i in changing_pos):

                # Self is a prime but not in primes (because we popped it)
                len_family = 1

                original_digits = digits.copy()

                # Change for every bit
                for digit in range(10):

                    # Except if we want to change the first bit to 0
                    if digit != 0 or changing_pos[0] != 0:
                        # Change every position
                        for changed_pos in changing_pos:
                            digits[changed_pos] = digit

                        # Construct the new number
                        nb = int("".join(list(map(str,digits))))
                        if nb in primes:
                            len_family += 1

                digits = original_digits

                # Save maximum
                if len_family > max_len:
                    max_len = len_family

    print("Result =", p, "in", time.time() - startTime)
