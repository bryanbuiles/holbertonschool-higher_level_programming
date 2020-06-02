#!/usr/bin/python3
""" 4 inherets_from
"""


def inherits_from(obj, a_class):
    """Return if the object is a instance of a class

    Arguments:
        obj {[instance]} -- instance of a class
        a_class {[object]} -- class

    Returns:
        True if is a intance of a clase otherwise False
    """
    if type(obj) is not a_class or isinstance(obj, a_class):
        return (True)
    else:
        False
