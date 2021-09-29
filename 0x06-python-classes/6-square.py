#!/usr/bin/python3

"""Empty class that defines a square"""


class Square:
    """Class that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Property that retieves the sieze"""
        return(self.__position)

    @position.setter
    def position(self, value):
        if ((type(value)is not tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in (value)) or
                (i < 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        for j in range(0, self.__position[1]):
            print("")
        for i in range(0, self.__size):
            for a in range(0, self.__position[0]):
                print(" ", end="")
            for k in range(0, self.__size):
                print('#', end="")
            print("")
