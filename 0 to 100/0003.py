'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''
def largest_prime_factor_0(k):
    '''
    Let n be the largest prime factor of k,
    Complexity : O(n)
    '''
    i = 1
    while i*i <= k:
        i += 1
        if k%i == 0:
            return max(i, largest_prime_factor_0(int(k/i)))
    return k

def largest_prime_factor_1(k):
    '''
    Let n be the largest prime factor of k,
    Complexity : O(sqrt(n))
    '''
    i = 1
    while i*i < k:
        i += 1
        if k%i == 0:
            k = int(k/i)
    return k

if __name__ == '__main__':
    result = largest_prime_factor_0(600851475143)
    result = largest_prime_factor_1(600851475143)
    print(result)
