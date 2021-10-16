#!/usr/bin/python3

"""Class that defines Base"""

import json
from os import write


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or bool(list_dictionaries) is False:
            my_list = []
            return(my_list)
        else:
            return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        filename = str(cls.__name__+".json")
        my_list = []
        if list_objs is None:
            with open(filename, mode="w", encoding="utf-8") as my_file:
                my_file.write(my_list)
        else:
            with open(filename, mode="w", encoding="utf-8") as my_file:
                for i in range(len(list_objs)):
                    my_list.append(cls.to_dictionary(list_objs[i]))
                my_file.write(cls.to_json_string(my_list))
    @staticmethod
    def from_json_string(json_string):
        my_list = []
        if json_string is None or bool(json_string) is False:
            return(my_list)
        else:
            return(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        