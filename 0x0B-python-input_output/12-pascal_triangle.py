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
    for i in range(max(n, 0)):
        my_list.append(x) 
        x = [left + rigth for left, rigth in zip(x + y, y + x)]
        return (my_list)
