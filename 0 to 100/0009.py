'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a² + b² = c²

For example, 3² + 4² = 9 + 16 = 25 = 5².

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
import numpy as np
import time

def find_pythagorean(k):
    ''' Naive version
    Complexity : O(k^3)
    '''
    for a in range(1, k):
        for b in range(a, k):
            for c in range(k):
                if a+b+c == k:
                    if a*a + b*b == c*c:
                        return a,b,c

def find_pythagorean_c(k):
    ''' Upgraded version, do not look for every c
    Complexity : O(k^2 * time of np.sqrt)
    '''
    for a in range(1, k):
        for b in range(a, k):
            c = np.sqrt(a*a+b*b)
            if a+b+c == k:
                return a,b,c

def find_pythagorean_good_c(k):
    ''' Upgraded version, only look for good c
    Complexity : O(k^2)
    '''
    for a in range(1, k):
        for b in range(a, k):
            c = k - a - b
            if a*a+b*b == c*c:
                return a,b,c

def find_pythagorean_good_c_keep_a(k):
    ''' Upgraded version, only look for good c
    Complexity : O(k^2)
    Do not recalculate a*a
    Fastest in practice
    '''
    for a in range(1, k):
        square_a = a*a
        for b in range(a, k):
            c = k - a - b
            if square_a+b*b == c*c:
                return a,b,c

def find_pythagorean_good_c_keep_a_bounded(k):
    ''' Upgraded version, only look for good c
    Complexity : O(k^2)
    Do not recalculate a*a
    Fastest in practice
    Better bounds if no triplet exists
    '''
    for a in range(1, k//2): # Because if a > k/2, we won't go in the other loop anyway
        square_a = a*a
        for b in range(a, k-a):
            c = k - a - b
            if square_a+b*b == c*c:
                return a,b,c

if __name__ == '__main__':
    startTime = time.time()
    result = find_pythagorean(1000)
    print(result, " in s:", time.time()-startTime)
    startTime = time.time()
    result = find_pythagorean_c(1000)
    print(result, " in s:", time.time()-startTime)
    startTime = time.time()
    result = find_pythagorean_good_c(10000)
    print(result, " in s:", time.time()-startTime)
    startTime = time.time()
    result = find_pythagorean_good_c_keep_a(10000)
    print(result, " in s:", time.time()-startTime)
    startTime = time.time()
    result = find_pythagorean_good_c_keep_a_bounded(10000)
    print(result, " in s:", time.time()-startTime)
