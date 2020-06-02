#!/usr/bin/python3
""" 10 square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """[summary]

    Arguments:
        Rectangle {[object]} -- class Rectangle
    """

    def __init__(self, size):
        """
        Arguments:
            size {[int]} -- Size of square
        """
        super().integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def __str__(self):
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
