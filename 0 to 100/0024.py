'''


A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
import math
import time

def perm_nb(vals, k):
    ''' Recursive algorithm to find the first element of the
    kth permutation'''

    if len(vals) == 1:
        return vals

    i = (k-1)//math.factorial(len(vals)-1) + 1
    if i == 0: # If none is found, it means the permutation is okay
        v0 = vals.pop(0)
        return [v0] + perm_nb(vals, k)
    else: # Else, we remove the first element and apply recursively
        res = vals.pop(i-1)
        return [res] + perm_nb(vals, k-(i-1)*math.factorial(len(vals)))

if __name__ == '__main__':
    startTime = time.time()
    result = perm_nb([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1000000)
    result = ''.join([str(elem) for elem in result])
    print(result, "in s:", time.time()-startTime)
