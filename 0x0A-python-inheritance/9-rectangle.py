#!/usr/bin/python3
""" 8 rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class

    Arguments:
        BaseGeometry {[class]} -- Base geometry class
    """

    def __init__(self, width, height):
        """contructor

        Arguments:
            width {[int]} -- width rectangle
            height {[int]} -- height rectangle
        """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns:
            [int] -- area rectangle
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        Returns:
            [str] -- magig str builtin
        """
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
