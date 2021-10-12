#!/usr/bin/python3

"""Class that defines Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square (Rectangle):
    """Class that defines Square"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return(self.__size * self.__size)

    def __str__(self):
        new_str = ""
        new_str = "[Square] {}/{}".format(str(self.__size),
                                          str(self.__size))
        return(new_str)
