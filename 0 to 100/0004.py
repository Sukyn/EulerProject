'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_palindrom(n):
    arr = list(str(n))
    for i in range(int(len(arr)/2)):
        if arr[i] != arr[len(arr)-1-i]:
            return False
    return True

def palindrom_product_0(k):
    ''' Naive version
    Complexity : 100**k loop iterations
    '''
    result = 0
    for i in range(10**k):
        for j in range(10**k):
            if is_palindrom(i*j):
                result = max(result, i*j)
    return result

def palindrom_product_1(k):
    '''
    Improved version since every
    palindrom must be divisible by 11
    Complexity : (100**k)/11 loop iterations
    '''
    result = 0
    for i in range(11, 10**k, 11):
        for j in range(10**k):
            if is_palindrom(i*j):
                result = max(result, i*j)
    return result

if __name__ == '__main__':
    result = palindrom_product_0(3)
    result = palindrom_product_1(3)
    print(result)
