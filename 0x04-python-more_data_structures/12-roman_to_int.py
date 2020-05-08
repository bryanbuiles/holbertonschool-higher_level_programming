#!/usr/bin/python3
def roman_to_int(roman_string):
    from functools import reduce
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    if not roman_string.isupper():
        return 0
    li = []
    for i in roman_string:
        li.append(i)
    count = r = t = a = flag = 0
    for k in li:
        try:
            if k == 'I' and (li[count + 1] == 'V' or li[count + 1] == 'X'):
                r += 1
                flag = 1
            if k == 'X' and (li[count + 1] == 'L' or li[count + 1] == 'C'):
                t += 1
                flag = 1
            if k == 'C' and (li[count + 1] == 'M' or li[count + 1] == 'D'):
                a += 1
                flag = 1
        except IndexError:
            pass
        if k == 'I':
            li[count] = 1
        elif k == 'V':
            li[count] = 5
        elif k == 'X':
            li[count] = 10
        elif k == 'L':
            li[count] = 50
        elif k == 'C':
            li[count] = 100
        elif k == 'D':
            li[count] = 500
        elif k == 'M':
            li[count] = 1000
        count += 1
    if flag == 1:
        j = int(reduce(lambda x, y: x+y, li) - (2*r) - (20*t) - (200*a))
    else:
        j = int(reduce(lambda x, y: x+y, li))
    return j
