#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError ("Each row of the matrix must have the same size")
    if not all((isinstance(i, int) or (isinstance(i, float)))
                for i in [j for row in matrix for j in row]):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise TypeError("ZeroDivisionError")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
