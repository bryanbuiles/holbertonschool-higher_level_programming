#!/usr/bin/python3
def search_replace(my_list, search, replace):
    count = 0
    newlist = my_list.copy()
    for i in my_list:
        if i == search:
            newlist[count] = replace
        count += 1
    return(newlist)
