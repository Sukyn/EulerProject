import time

if __name__ == '__main__':

    startTime = time.time()
    result = set()
    for a in range(2, 101):
        for b in range(2, 101):
            c = a**b
            if c not in result:
                result.add(c)
    print(len(result), "in", time.time() - startTime)
