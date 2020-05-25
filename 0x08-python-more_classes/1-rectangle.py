#!/usr/bin/python3
""" 0-rectanule.py
    Rectangule class
"""


class Rectangle:
    """Rectangule Class"""

    def __init__(self, width=0, height=0):
        """__init__ Contructor
        Contructor of class Square
        Args:
            width (integer): privete attribute width
            height (int): private attribute height
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """ Getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter module for set height
            Args:
                Value: height of rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ Getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter module for set a width
            Args:
                Value: width of rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
