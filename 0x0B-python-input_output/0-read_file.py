#!/usr/bin/python3
"""
Function that reads a text file
(UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """Function that reads a text file
    (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as my_file:
        lines = my_file.read()
        print(lines)
