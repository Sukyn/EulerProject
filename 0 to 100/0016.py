'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
'''
import time

def digit_numbers(k):
    return sum(map(int, str(k)))

if __name__ == '__main__':
    startTime = time.time()
    k = 2
    result = digit_numbers(2**1000)
    print("20 :", result, "in s:", time.time()-startTime)
