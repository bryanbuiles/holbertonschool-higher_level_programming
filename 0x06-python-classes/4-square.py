#!/usr/bin/python3
""" 3-square.py
    Square class

    Module Area: return current area square
    Module size: module to retrieve it or set the value
"""


class Square:
    """Square Class"""

    def __init__(self, size=0):
        """__init__ Contructor
        Contructor of class Square
        Args:
            size (integer): privete attribute for size Square
        """
        self.__size = size

    def area(self):
        """Return The area of square"""
        return(self.__size * self.__size)

    @property
    def size(self):
        """ Put a __ before this private field"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter module for set a size
        Args:
            Value: Size of square
            """
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
