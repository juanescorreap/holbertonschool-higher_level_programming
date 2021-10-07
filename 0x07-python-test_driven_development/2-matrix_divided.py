#!/usr/bin/python3
"""
Function that divides all the elements of
a matrix by an integer lager than zero
and returns a new matrix with the results
"""


def matrix_divided(matrix, div):
    """Function that divides all the elements of
    a matrix by an integer lager than zero
    and returns a new matrix with the results"""

    error_string = "matrix must be a matrix (list of lists) of integers/floats"

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not all((isinstance(i, int) or (isinstance(i, float)))
               for i in [j for row in matrix for j in row]):
            raise TypeError(error_string)
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise TypeError("ZeroDivisionError")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
