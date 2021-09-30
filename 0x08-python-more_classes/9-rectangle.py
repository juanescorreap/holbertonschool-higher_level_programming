#!/usr/bin/python3

"""Class that defines a rectangle"""


class Rectangle:
    """Class that defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return(self.__height * self.__width)

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return(0)
        return((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        new_str = ""
        if self.__width == 0 or self.__height == 0:
            return(new_str)
        for j in range(0, self.__height):
            for i in range(0, self.__width):
                new_str = new_str + str(self.print_symbol)
            new_str = new_str + "\n"
        new_str = new_str[0:-1]
        return(new_str)

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return(rect_1)
        if rect_1.area() < rect_2.area():
            return(rect_2)
        if rect_1.area() == rect_2.area():
            return(rect_1)

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
