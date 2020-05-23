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
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")
    else:
        a = int(round(a))
        b = int(round(b))
    return (a + b)
