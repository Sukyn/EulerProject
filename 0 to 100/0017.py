'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

dic = {}

if __name__ == '__main__':
    dic[0] = 0
    dic[1] = len("one")
    dic[2] = len("two")
    dic[3] = len("three")
    dic[4] = len("four")
    dic[5] = len("five")
    dic[6] = len("six")
    dic[7] = len("seven")
    dic[8] = len("eigth")
    dic[9] = len("nine")
    dic[10] = len("ten")
    dic[11] = len("eleven")
    dic[12] = len("twelve")
    dic[13] = len("thirteen")
    dic[14] = len("fourteen")
    dic[15] = len("fifteen")
    dic[16] = len("sixteen")
    dic[17] = len("seventeen")
    dic[18] = len("eighteen")
    dic[19] = len("nineteen")
    dic[20] = len("twenty")
    dic[30] = len("thirty")
    dic[40] = len("forty")
    dic[50] = len("fifty")
    dic[60] = len("sixty")
    dic[70] = len("seventy")
    dic[80] = len("eigthy")
    dic[90] = len("ninety")
    hundred = len("hundred")
    thousand = len("thousand")
    ands = len("and")
    for i in range(21, 1001):
        if i == 1000:
            dic[i] = dic[1] + thousand
        elif i%100 == 0:
            dic[i] = dic[i//100] + hundred
        elif i//100 >= 1:
            dic[i] = dic[i//100] + hundred + ands + dic[i%100]
        elif i%10 != 0:
            dic[i] = dic[(i//10) * 10] + dic[i%10]
    result = sum(dic.values())
    print(dic)
    print(result)
