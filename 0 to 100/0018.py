'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

    3
   7 4
  2 4 6
 8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                     75
                    95 64
                  17 47 82
                18 35 87 10
               20 04 82 47 65
             19 01 23 75 03 34
            88 02 77 73 07 63 67
          99 65 04 28 06 16 70 92
         41 41 26 56 83 40 80 70 33
       41 48 72 33 47 32 37 16 94 29
      53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
   91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''
import time


def brute_force_path(tab):
    if len(tab) == 1:
        return tab

    tab0 = tab.pop(0)

    left_path = brute_force_path([line[1:] for line in tab])
    left = [tab0 + left_p for left_p in left_path]
    right_path = brute_force_path([line[:-1] for line in tab])
    right = [tab0 + right_p for right_p in right_path]

    return left + right

def brute_force():
    ''' Naive solution :
    Brute force
    Complexity : 2^24
    '''
    nbs = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]
    paths = brute_force_path(nbs)
    return max([sum(path) for path in paths])

def dynamic_programming_algo(tab):
    #print(tab)
    if len(tab) == 1:
        #print(tab, max(tab[0][0], tab[0][1]), 0, 0)
        return tab[0][0]

    tab0 = tab.pop(0)
    left_max = dynamic_programming_algo([line[1:] for line in tab])
    right_max = dynamic_programming_algo([line[:-1] for line in tab])
    #print(tab, tab0[0], left_max, right_max)
    return tab0[0] + max(left_max, right_max)

def dynamic_programming():
    nbs = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]
    return dynamic_programming_algo(nbs)

if __name__ == '__main__':
    startTime = time.time()
    result = brute_force()
    print(result, "in s:", time.time()-startTime)
    startTime = time.time()
    result = dynamic_programming()
    print(result, "in s:", time.time()-startTime)
