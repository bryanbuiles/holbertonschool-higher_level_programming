#!/usr/bin/python3
"""
    My div module matrix
    matrix_divided: function that div elements of a matrix
    Return: the div of two intigers
"""


def matrix_divided(matrix, div):
    """ Return the div of each element of matrix
        matrix: list of list of int and float
        div: number != 0
    """

    message = "matrix must be a matrix (list of lists) of integers/floats"
    rlen = -1
    if type(matrix) != list:
        raise TypeError(message)
    for items in matrix:
        if type(items) != list:
            raise TypeError(message)
        if (rlen != len(items) and rlen != -1):
            raise TypeError("Each row of the matrix must have the same size")
        rlen = len(items)
        for i in items:
            if not isinstance(i, (int, float)) or isinstance(i, bool):
                raise TypeError(message)
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    return ([[round(i / div, 2) for i in row] for row in matrix])
