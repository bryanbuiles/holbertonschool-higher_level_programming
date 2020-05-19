#!/usr/bin/python3
""" 3-square.py
    Square class

    Module Area: return current area square
"""


class Square:
    """Square Class"""

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

    def area(self):
        """Return The area of square"""
        return(self.__size * self.__size)
