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
        if list_objs is None:
            my_list= []
            with open(filename, mode="w", encoding="utf-8") as my_file:
                my_file.write(my_list)
        else:
            with open(filename, mode="w", encoding="utf-8") as my_file:
                my_file.write(cls.to_json_string(list_objs))