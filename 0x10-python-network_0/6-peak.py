#!/usr/bin/python3
""" Find the peak """


def find_peak(list_of_integers):
    """ function to find the pick """
    if len(list_of_integers) == 0:
        return None
    list_of_integers.sort()
    return(list_of_integers[-1])
