#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        list1 = list(t[0] * t[1] for t in my_list)
        lis2 = list(t[1] for t in my_list)
        average = sum(list1) / sum(lis2)
        return average
    else:
        return 0
