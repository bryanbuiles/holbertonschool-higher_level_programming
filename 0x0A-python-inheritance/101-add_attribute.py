#!/usr/bin/python3
""" 101 add atributte"""


def add_attribute(obj, name, hello):
    """
    Arguments:
        obj {[objecto]}
        name {[str]}
        hello {[str]}

    Raises:
        TypeError: can add new atributte
    """
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, name, hello)
