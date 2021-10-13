#!/usr/bin/python3
"""
Function that returns a list of lists of
integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """Function that returns a list of lists of
    integers representing the Pascal’s triangle of n"""
    x = [1]
    y = [0]
    my_list = []
    i = 0
    while i < n:
        my_list.append(x)
        x = [left + rigth for left, rigth in zip(x + y, y + x)]
        i = i + 1
    return (my_list)
