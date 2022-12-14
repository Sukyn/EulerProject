import math
maximum = 0
max_val = 0
i = 0

def dynamic_programming_algo(previous_length, tab):
    ''' Naive approach
    Slightly optimized bruteforce'''
    global maximum
    global max_val
    global i
    print(maximum, i*100/math.pow(2,100), "%")

    i += 1
    if len(tab) == 1:
        maximum = max(maximum, previous_length + tab[0][0])
        return tab[0][0]

    if previous_length + max_val*len(tab) > maximum:
        tab0 = tab.pop(0)

        if tab[0][0] < tab[0][1]:
            left_max = dynamic_programming_algo(previous_length + tab0[0], [line[1:] for line in tab])
            right_max = dynamic_programming_algo(previous_length + tab0[0], [line[:-1] for line in tab])
        else:
            right_max = dynamic_programming_algo(previous_length + tab0[0], [line[:-1] for line in tab])
            left_max = dynamic_programming_algo(previous_length + tab0[0], [line[1:] for line in tab])


def dynamic_prog_optimized(tab):
    ''' Best version :
    Calculate row by row from bottom
    Complexity O(n^2)'''
    if len(tab) == 1:
        return tab[0][0]
    else:
        for i in range(len(tab[-2])):
            tab[-2][i] = tab[-2][i] + max(tab[-1][i], tab[-1][i+1])
        tab.pop(len(tab)-1)
        return dynamic_prog_optimized(tab)

if __name__ == '__main__':
    #global max_val
    with open('triangle067.txt') as f:
        lines = f.readlines()
    vals = [line.split() for line in lines]

    for j, line in enumerate(vals):
        line = [int(i) for i in line]
        vals[j] = line


    for line in vals:
        max_val = max(max_val, max(line))

    #print(vals)
    result = dynamic_prog_optimized(vals)
    print(result)
    #
    #dynamic_programming_algo(0, vals)
    #print(maximum)
