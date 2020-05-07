#!/usr/bin/python3
def uniq_add(my_list=[]):
    newlist = set(my_list)
    p = 0
    for i in newlist:
        p = p + i
    return (p)
