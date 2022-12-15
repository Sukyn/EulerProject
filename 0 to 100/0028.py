
'''upper right = (i-2)^2 + 4(i^2 - (i-2)^2)/4 = i^2'''
def sum_upper_right(k):
    return sum([i**2 for i in range(1, k+1, 2)])
'''
lower left = (i-2)^2 + 2(i^2 - (i-2)^2)/4
		   = (i^2+(i-2)^2) / 2
'''
def sum_lower_left(k):
    return sum([(i**2+(i-2)**2)//2 for i in range(1, k+1, 2)])
'''
lower right =  (i-2)^2 + 1(i^2 - (i-2)^2)/4
		(i^2+3(i-2)^2)/4
		(25 + 3*9)/4
		(25+27)/4
		52/4
		26/2
		13
'''
def sum_lower_right(k):
    return sum([(i**2+3*((i-2)**2))//4 for i in range(1, k+1, 2)])
'''
upper left = (i-2)^2 + 3(i^2 - (i-2)^2)/4
	     (3i^2+(i-2)^2)/4
	     (75 + 9)/4
	     (84)/4
             (42)/2
'''
def sum_upper_left(k):
    return sum([(3*(i**2)+(i-2)**2)//4 for i in range(1, k+1, 2)])

'''
Direct sum (adding everything together)
4i² -6i + 6
'''
def sum_total(k):
    return sum([4*(i**2)-6*i+6 for i in range(1, k+1, 2)])

if __name__ == '__main__':
    result = 1
    result += sum_total(1001)
    result -= 4
    print(result)
