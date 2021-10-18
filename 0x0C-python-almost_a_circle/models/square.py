#!/usr/bin/python3
"""Class that defines Square"""

from models.rectangle import Rectangle


class Square (Rectangle):
    """Class that defines Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor for the square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """STR method to print a Square"""
        return("[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id,
                                             self.x, self.y, self.width))

    @property
    def size(self):
        """Getter for size"""
        return(self.width)

    @size.setter
    def size(self, value):
        """"Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Method to up date a square"""
        if args is None:
            for key, value in kwargs.items():
                if key == "size":
                    self.width = value
                if key == "size":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
                if key == "id":
                    self.id = value
        else:
            for i in range(len(args)):
                if i == 2:
                    self.width = args[2]
                if i == 2:
                    self.height = args[2]
                if i == 3:
                    self.x = args[3]
                if i == 4:
                    self.y = args[4]
                if i == 1:
                    self.id = args[1]

    def to_dictionary(self):
        """Method to return the dictionary"""
        return(self.__dict__)
