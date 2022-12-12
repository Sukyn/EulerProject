'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''
import time

def get_chain_length(k):
    i = 1
    while (k > 1):
        if k%2 == 0:
            k = k//2
        else:
            k = 3*k + 1
        i += 1
    return i

def find_best(k):
    ''' Naive implementation
    Brute force
    '''
    maximum_i = 0
    maximum_val = 0
    for i in range(k):
        length = get_chain_length(i)
        if maximum_val < length:
            maximum_val = length
            maximum_i = i
    return maximum_i


memo = {}

def get_chain_length_memo(k):
    i = 1
    while (k > 1):

        if k in memo:
            return memo[k]+i

        if k%2 == 0:
            k = k//2
        else:
            k = 3*k + 1
        i += 1
    return i

def find_best_memo(k):
    ''' Upgraded version
    Memoisation of values
    '''
    maximum_i = 0
    maximum_val = 0
    for i in range(k):
        length = get_chain_length_memo(i)
        memo[i] = length
        if maximum_val < length:
            maximum_val = length
            maximum_i = i
    return maximum_i

def find_best_memo_rev(k):
    ''' Upgraded version
    Memoisation of values
    Reverse order, should be way faster
        because we know high values quickly
    '''
    maximum_i = 0
    maximum_val = 0
    for i in range(k-1, 0, -1):
        length = get_chain_length_memo(i)
        memo[i] = length
        if maximum_val < length:
            maximum_val = length
            maximum_i = i
    return maximum_i

if __name__ == '__main__':
    startTime = time.time()
    result = find_best(1000000)
    print(result, "in s:", time.time()-startTime)
    startTime = time.time()
    result = find_best_memo(10000000)
    print(result, "in s:", time.time()-startTime)
    startTime = time.time()
    result = find_best_memo_rev(10000000)
    print(result, "in s:", time.time()-startTime)
