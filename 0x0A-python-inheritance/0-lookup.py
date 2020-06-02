#!/usr/bin/python3
""" Lookup
"""


def lookup(obj):
    """ Returns the list of available attributes
        and methods of an object
    """
    i = dir(obj)
    return(i)
