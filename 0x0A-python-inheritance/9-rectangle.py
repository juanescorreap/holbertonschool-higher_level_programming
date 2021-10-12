#!/usr/bin/python3

"""Class that defines Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that defines Rectangle"""
    def __init__(self, width, height):
        super().integer_validator(self, "width", width)
        super().integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return(self.__width * self.__height)

    def __str__(self):
        new_str = ""
        new_str = "[{}] {}/{}".format(str(type(self).__name__),
                                      str(self.__width), str(self.__height))
        return(new_str)

    def print(self):
        print(self)
