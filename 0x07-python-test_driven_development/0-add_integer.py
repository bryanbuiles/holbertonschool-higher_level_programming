#!/usr/bin/python3
"""
    My add module
    add_integer: function that add two numbers
    Return: the add of two intigers
"""


def add_integer(a, b=98):
    """ Return the add of intigers
        a and b are intigers
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        a = int(round(a))
        b = int(round(b))
    return (a + b)
