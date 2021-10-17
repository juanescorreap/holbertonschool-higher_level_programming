#!/usr/bin/python3
"""Class that defines Base"""

from models.base import Base


class Rectangle (Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return(self.__x)

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return(self.__y)

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return (self.width * self.height)

    def display(self):
        for k in range(0, self.y):
            print()
        for i in range(0, self.height):
            for l in range(0, self.x):
                print(" ", end="")
            for j in range(0, self.width):
                print("#", end="")
            print("")

    def __str__(self):
        return("[{}] ({}) {}/{} - {}/{}".format(type(self).__name__,
                                                self.id, self.x, self.y,
                                                self.width, self.height))

    def update(self, *args):
        for i in range(len(args)):
            if i == 2:
                self.width = args[2]
            if i == 3:
                self.height = args[3]
            if i == 4:
                self.x = args[4]
            if i == 5:
                self.y = args[5]
            if i == 1:
                super().__init__(args[1])

    def update(self, *args, **kwargs):
        for key, value in kwargs.items():
            if key == "width":
                self.width = value
            if key == "height":
                self.height = value
            if key == "x":
                self.x = value
            if key == "y":
                self.y = value
            if key == "id":
                super().__init__(value)

        for i in range(len(args)):
            if i == 2:
                self.width = args[2]
            if i == 3:
                self.height = args[3]
            if i == 4:
                self.x = args[4]
            if i == 5:
                self.y = args[5]
            if i == 1:
                super().__init__(args[1])

    def to_dictionary(self):
        return(self.__dict__)
