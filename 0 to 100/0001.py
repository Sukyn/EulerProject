'''
If we list all the natural numbers below 10 that are multiples of 3 or 5,
 we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

def counting_0(k):
    ''' Naive implementation :
    We iterate over the k first numbers, and check
    if they are multiple of 3 or 5
    '''
    # Complexity : k-1 loop iterations
    result = 0
    # k-1 iterations
    for i in range(1, k):
        if i%3 == 0 or i%5 == 0:
            result += i
    return result

def counting_1(k):
    '''
    We iterate over multiple of 3, then on
    multiple of 5 and check if they are multiple of 3
    '''
    # Complexity : 8/15*k - 1 loop iterations
    result = 0
    # (k-1)/3 iterations
    for i in range(3, k, 3):
        result += i
    # (k-1)/5 iterations
    result = 0
    for i in range(5, k, 5):
        if i%3 != 0:
            result += i
    return result

def counting_2(k):
    '''
    We use a formula to compute the sum of
    multiples of each element, and only do
    a few additions
    '''
    # Complexity : 0 loop iterations
    result = 0

    # Calculating the sum of multiple of 3
    n = int((k-1)/3)
    first_term = 3
    last_term = (k-1)-(k-1)%3
    sum_of_3_multiples = n/2*(first_term + last_term)

    result += sum_of_3_multiples

    # Calculating the sum of multiple of 5
    n = int((k-1)/5)
    first_term = 5
    last_term = (k-1)-(k-1)%5
    sum_of_5_multiples = n/2*(first_term + last_term)

    result += sum_of_5_multiples

    # Calculating the sum of multiple of 3 and 5
    n = int((k-1)/15)
    first_term = 15
    last_term = (k-1)-(k-1)%15
    sum_of_5_and_3_multiples = n/2*(first_term + last_term)

    result -= sum_of_5_and_3_multiples

    return int(result)

if __name__ == '__main__':
    result = counting_0(1000)
    result = counting_1(1000)
    result = counting_2(1000)

    print(result)
