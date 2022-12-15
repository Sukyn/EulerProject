'''

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
'''

if __name__ == '__main__':

    number = sum([i**i for i in range(1, 1001)])
    last_digits = list(map(int, str(number).strip()))[-10:]
    print(int("".join(list(map(str,last_digits)))))
