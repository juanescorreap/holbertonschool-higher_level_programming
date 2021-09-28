#!/usr/bin/python3

"""Empty class that defines a square"""


class Square:
    """Class that defines a square"""
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """Public instance method that returns the current square area"""
        return(self.__size * self.__size)

    @property
    def size(self):
        """Property that retrieves the size"""
        return(self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            print("size must be an integer", end="")
            raise TypeError
        if value < 0:
            print("size must be >= 0", end="")
            raise ValueError
        self.__size = value

    def my_print(self):
        for i in range(0, self.__size):
            for i in range(0, self.__size):
                print("#", end="")
            print()
