#!/usr/bin/python3
"""
Function that prints two stings as
first and last names
"""


def say_my_name(first_name, last_name=""):
    """Function that prints two stings as
    first and last names"""

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
