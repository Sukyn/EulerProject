'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''
import time
import numpy as np

def count_ways_binomial(length):
    ''' Mathematical way '''
    return np.math.factorial(2*length)/(np.math.factorial(length)**2)

def count_ways(len_vert, len_horiz):
    ''' Computer Science way '''
    longer = max(len_vert, len_horiz)

    paths = [[(len_vert-i,i)] for i in range(longer+1//2)]
    for i in range(longer+1, len_vert + len_horiz+1):
        print(i, len(paths))
        destroy = paths.copy()
        for path in destroy:
            last_x, last_y = path[-1]
            if last_x < len_vert:
                paths.append(path + [(last_x + 1, last_y)])
            if last_y < len_horiz:
                paths.append(path + [(last_x, last_y+1)])
            paths.pop(0)

    sum = 2**(longer-1)
    for path in paths:
        if path[0] == (longer//2, longer//2):
            sum += 1
        else:
            sum += 2
    return sum

if __name__ == '__main__':
    startTime = time.time()
    result = count_ways_binomial(20)
    print("20 :", result, "in s:", time.time()-startTime)
