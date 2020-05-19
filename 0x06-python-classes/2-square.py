#!/usr/bin/python3
""" 2-square.py
    Square class 
"""


class Square:
    """Square Class
    Class 
    """

    def __init__(self, size=0):
        """__init__ Contructor
        Contructor of class Square
        Args:
            size (integer): privete attribute for size Square
        """
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
