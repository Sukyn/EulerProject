

# 1, 2, 5, 10, 20, 50, 100, 200
import time

if __name__ == '__main__':

    startTime = time.time()
    count = 0
    for ones in range(0, 201, 1):
        for twos in range(0, 201-ones, 2):
            for fives in range(0, 201-twos-ones, 5):
                for tens in range(0, 201-twos-ones-fives, 10):
                    for twenties in range(0, 201-twos-ones-fives-tens, 20):
                        for fifties in range(0, 201-twos-ones-fives-tens-twenties, 50):
                            for hundreds in range(0, 201-twos-ones-fives-tens-twenties-fifties, 100):
                                for twohundreds in range(0, 201-twos-ones-fives-tens-twenties-fifties-hundreds, 200):
                                    if ones+twos+fives+tens+twenties+fifties+hundreds+twohundreds == 200:
                                        count+=1
    print(count, time.time() - startTime)
