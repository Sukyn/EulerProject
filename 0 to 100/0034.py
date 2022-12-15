

def fact(n, acc):
    if n == 0:
        return acc
    return fact(n-1, acc*n)

def is_sum_of_digits_fact(n):
    digits = list(map(int, str(n).strip()))
    return n == sum([fact(i, 1) for i in digits])


if __name__ == '__main__':

    result = 0
    for i in range(3, 7*fact(9, 1)):
        #print(i)
        if is_sum_of_digits_fact(i):
            print(i)
            result += i
    print(result)
