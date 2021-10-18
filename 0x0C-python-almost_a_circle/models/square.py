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
        if args is not None and len(args) > 0:
            for i in range(len(args)):
                if i == 1:
                    self.width = args[1]
                if i == 1:
                    self.height = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
                if i == 0:
                    self.id = args[0]
        else:
            for key, value in kwargs.items():
                if key == "size":
                    setattr(self, key, value)
                if key == "size":
                    setattr(self, key, value)
                if key == "x":
                    setattr(self, key, value)
                if key == "y":
                    setattr(self, key, value)
                if key == "id":
                    setattr(self, key, value)

    def to_dictionary(self):
        """Method to return the dictionary"""
        new_dict = {}
        for key, value in self.__dict__.items():
            if key[:12] == "_Rectangle__":
                new_dict[key[12:]] = value
            else:
                new_dict[key] = value
        new_dict["size"] = new_dict["width"]
        del new_dict["width"], new_dict["height"]
        return(new_dict)
