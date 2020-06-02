#!/usr/bin/python3
"""is kind of class
"""


def is_kind_of_class(obj, a_class):
    """Return if the object is a instance of a class

    Arguments:
        obj {[instance]} -- instance of a class
        a_class {[object]} -- class

    Returns:
        True if is a intance of a clase otherwise False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
