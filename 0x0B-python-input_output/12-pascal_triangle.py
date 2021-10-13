#!/usr/bin/python3
"""
Function that returns a list of lists of
integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    if n <= 0:
        x = []
        return (x)
    x = [1]
    y = [0]
    for i in range(n):
        print(x)
        x = [left + rigth for left, rigth in zip(x + y, y + x)]
        return (n >= 1)
