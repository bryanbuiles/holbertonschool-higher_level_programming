#!/usr/bin/python3
""" Find the peak """


def find_peak(list_of_integers):
    """ function to find the pick """
    temp = 0
    if len(list_of_integers) == 0:
        return None
    for i in list_of_integers:
        if i > temp:
            temp = i
    return temp
