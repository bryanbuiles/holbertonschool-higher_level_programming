#!/usr/bin/python3
""" 1-square.py
    Square class with private attribute size
"""


class Square:
    """Square Class
    Class with private attribute size
    """

    def __init__(self, size):
        """__init__ Contructor
        Contructor of class Square
        Args:
            size (integer): privete attribute for zise Square
        """
        self.__size = size
