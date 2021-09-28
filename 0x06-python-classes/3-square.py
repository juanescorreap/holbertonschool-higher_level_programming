#!/usr/bin/python3
class Square:
    """Class that defines a square"""
    def __init__(self, size=0):
        if type(size) is not int:
            print("size must be an integer", end="")
            raise TypeError
        if size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        self.__size = size

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size * self.__size
