#!/usr/bin/python3
"""
    Say_my_name module
    say_my_name: function that prints my name
    Return: nothing
"""


def say_my_name(first_name, last_name=""):
    """
        function that Print names
        first_name: The first name
        last_name: The last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
