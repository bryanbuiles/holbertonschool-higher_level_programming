#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newlist = my_list.copy()
    for i in newlist:
        if i % 2 == 0:
            newlist[i] = True
        else:
            newlist[i] = False
    return(newlist)
