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
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    message = "matrix must be a matrix (list of lists) of integers/floats"
    rlen = -1
    for items in matrix:
        if type(items) != list:
            raise TypeError(message)
        if (rlen != len(items) and rlen != -1):
            raise TypeError("Each row of the matrix must have the same size")
        rlen = len(items)
        for i in items:
            if not isinstance(i, int) and not isinstance(i, float):
                raise TypeError(message)
    return ([[round(i / div, 2) for i in row] for row in matrix])
