#!/usr/bin/python3
"""
    Say_my_name module
    say_my_name: function that prints my name
    Return: nothing
"""


def print_square(size):
    """ Print the square with #
        size: size of square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size == 0:
        return
    for i in range(size):
        print("#" * size)
