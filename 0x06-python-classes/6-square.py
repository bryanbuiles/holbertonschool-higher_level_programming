#!/usr/bin/python3
"""
    Square class

    Module Area: return current area square
    Module size: module to retrieve it or set the value
    Module print: public Module that prints the square
    Module position: with property  and property setter

"""


class Square:
    """Square Class"""

    def __init__(self, size=0, position=(0, 0)):
        """__init__ Contructor
        Contructor of class Square
        Args:
            position (tuple): private attrinute to posicion
            size (integer): privete attribute for size Square
        """
        self.size = size
        self.position = position

    def area(self):
        """Return The area of square"""
        return(self.__size * self.__size)

    @property
    def size(self):
        """ Put a __ before this private field"""
        return self.__size

    @property
    def position(self):
        """ retrieve position """
        return self.__position

    @position.setter
    def position(self, value):
        """setter module for position
            Args:
                value (tuple): position in x, y
            """
        message = "position must be a tuple of 2 positive integers"
        if type(value) != tuple or len(value) != 2:
            raise TypeError(message)

        for items in value:
            if type(items) != int or items < 0:
                raise TypeError(message)

        self.__position = value

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

    def my_print(self):
        """ Print the square with # and also with the position"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
        for row in range(self.__size):
            print((' ' * self.__position[0]) + ('#' * self.__size))
