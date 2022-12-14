'''
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def diff_integer(k):
    int_sum = k * (k + 1) * (2*k + 1) // 6
    squares_sum = (k*(k+1)//2)**2
    return squares_sum - int_sum

if __name__ == '__main__':
    result = diff_integer(100)
    print(result)
