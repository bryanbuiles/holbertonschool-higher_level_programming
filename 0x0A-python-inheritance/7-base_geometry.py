#!/usr/bin/python3
"""[summary]

    Raises:
        Exception: [description]
"""


class BaseGeometry:
    """ BaseGeometry class
    """

    def area(self):
        """ Raise a excepcion

        Raises:
            Exception: Area in not implement
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer validator

        Arguments:
            name {str} -- Str name value
            value {int} -- value number

        Raises:
            TypeError: Value must be a integer
            ValueError: Value mus be greather than 0
        """
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
