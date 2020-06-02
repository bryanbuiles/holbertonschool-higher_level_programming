#!/usr/bin/python3
""" 1-my list
"""


class MyList(list):
    """Mylist

    Arguments:
        list (list) -- pattern class list
    """

    def print_sorted(self):
        """ print soted list
        """
        print(sorted(self))
