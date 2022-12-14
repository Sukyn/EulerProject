
'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''
import time

def fact(n):
    ''' Naive factorial'''
    if n == 0:
        return 1
    return n*fact(n-1)

def fact_tailed(n, acc):
    ''' No pending requests '''
    if n == 0:
        return acc
    return fact_tailed(n-1, acc*n)

if __name__ == '__main__':
    startTime = time.time()
    result = sum(list(map(int, str(fact(100)).strip())))
    print(result, "in s:", time.time()-startTime)
    startTime = time.time()
    result = sum(list(map(int, str(fact_tailed(100, 1)).strip())))
    print(result, "in s:", time.time()-startTime)
