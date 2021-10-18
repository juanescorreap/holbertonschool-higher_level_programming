#!/usr/bin/python3

"""Class that defines Base"""

import json


class Base:
    """Class that defines Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor for the Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file:"""
        filename = str(cls.__name__)+".json"
        my_list = []
        if list_objs is not None:
            for i in range(len(list_objs)):
                my_list.append(cls.to_dictionary(list_objs[i]))
        with open(filename, mode="w", encoding="utf-8") as my_file:
            my_file.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        my_list = []
        if json_string is None or bool(json_string) is False:
            return(my_list)
        else:
            return(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            new_instance = cls(5, 5)
        else:
            new_instance = cls(5)
        new_instance.update(**dictionary)
        return(new_instance)

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        my_list = []
        filename = str(cls.__name__+".json")
        with open(filename, encoding="utf-8") as my_file:
            lines = my_file.read()
            dictionay = cls.from_json_string(lines)
            for i in dictionay:
                my_list.append(cls.create(**i))
        return(my_list)
