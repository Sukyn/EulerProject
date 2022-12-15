

def is_sum_of_power(n, k):
    digits = list(map(int, str(n).strip()))
    return sum(digit**k for digit in digits) == n

if __name__ == '__main__':

    result = 0
    for i in range(2, 6*(9**5)):
        if is_sum_of_power(i, 5):
            print(i)
            result += i
    print(result)
