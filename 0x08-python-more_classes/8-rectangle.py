#!/usr/bin/python3
""" 0-rectanule.py
    Rectangule class
"""


class Rectangle:
    """Rectangule Class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """__init__ Contructor
        Contructor of class Square
        Args:
            width (integer): privete attribute width
            height (int): private attribute height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ Return area of rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Return the perimiter of rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """ Print the rectangle with # """
        r = ""
        if self.__height == 0 or self.__width == 0:
            return (r)
        else:
            for i in range(self.__height):
                for k in range(self.__width):
                    r += str(self.print_symbol)
                if i != self.__height - 1:
                    r += "\n"
            return(r)

    def __repr__(self):
        """ eval is magic """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """ deletes intances of rectangle """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ compare two rectangles """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2
