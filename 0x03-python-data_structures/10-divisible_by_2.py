#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newlist = my_list.copy()
    j = 0
    for i in my_list:
        if i % 2 == 0:
            newlist[j] = True
        else:
            newlist[j] = False
        j += 1
    return(newlist)
