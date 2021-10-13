#!/usr/bin/python3

"""Class that defines Student"""


class Student:
    """Class that defines Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return(self.__dict__)
        else:
            return({i: self.__dict__[i] for i in self.__dict__ if i in attrs})
