#!/usr/bin/python3

"""Class that defines Student"""


class Student:
    """Class that defines Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if all(i is str for i in attrs):
            return ({i for i in self.__dict__ if i in attrs})
        else:
            return(self.__dict__)
