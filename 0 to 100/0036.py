import time

def is_palindrom_base_10(n):
    arr = list(str(n))
    return arr == arr[::-1]

def is_palindrom_base_2(n):
    arr = list(format(n, 'b'))
    return arr == arr[::-1]

if __name__ == '__main__':
    result = 0

    startTime = time.time()
    for i in range(1, 1000000, 2): # An even number will be like 1..0 in binary
        if is_palindrom_base_10(i) and is_palindrom_base_2(i):
            print(i)
            result += i
    print(result, "in", time.time() - startTime)
