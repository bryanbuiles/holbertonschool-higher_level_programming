#!/usr/bin/python3
"""
    Returns: [bool]
"""


class MyInt(int):
    """
    Arguments:
        int {[class object]}
    """

    def __eq__(self, value):
        return False

    def __ne__(self, value):
        return True
