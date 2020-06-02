#!/usr/bin/python3
""" Same class """


def is_same_class(obj, a_class):
    """Return if the object is a instance of a class

    Arguments:
        obj {[instance]} -- instance of a class
        a_class {[object]} -- class

    Returns:
        True if is a intance of a clase otherwise False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
