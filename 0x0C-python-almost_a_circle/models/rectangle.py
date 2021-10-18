#!/usr/bin/python3
"""Class that defines Base"""

from models.base import Base


class Rectangle (Base):
    """Class that defines Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor for the Rectangle class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for width"""
        return(self.__width)

    @width.setter
    def width(self, value):
        """Setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return(self.__height)

    @height.setter
    def height(self, value):
        """Setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return(self.__x)

    @x.setter
    def x(self, value):
        """setter for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return(self.__y)

    @y.setter
    def y(self, value):
        """setter for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Method that returns the area of a rectangle"""
        return (self.width * self.height)

    def display(self):
        """Method that prints the rectangle on stdout"""
        for k in range(0, self.y):
            print()
        for i in range(0, self.height):
            for l in range(0, self.x):
                print(" ", end="")
            for j in range(0, self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """STR method to print a Rectangle"""
        return("[{}] ({}) {}/{} - {}/{}".format(type(self).__name__,
                                                self.id, self.x, self.y,
                                                self.width, self.height))

    def update(self, *args):
        """Method to up date a Rectangle"""
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
        """Method to up date a Rectangle"""
        if args is not None and len(args) > 0:
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
                    self.id = args[1]
                print("->{}".format(args[i]))
        else:
            for key, value in kwargs.items():
                if key == "width":
                    setattr(self, key, value)
                if key == "height":
                    setattr(self, key, value)
                if key == "x":
                    setattr(self, key, value)
                if key == "y":
                    setattr(self, key, value)
                if key == "id":
                    setattr(self, key, value)

    def to_dictionary(self):
        """Method to return the dictionary"""
        return(self.__dict__)
