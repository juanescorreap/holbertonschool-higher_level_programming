#!/usr/bin/python3
"""
Function adds two newlines after every
? . : character.
"""


def text_indentation(text):
    """Function adds two newlines after every
    ? . : character."""

    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text) and text[i] == ' ':
        i = i + 1
    while i < len(text):
        print("{:s}".format(text[i]), end="")
        if (text[i] == "\n" or text[i] == '?' or text[i] == ':' or
                text[i] == '.'):
            if text[i] == '?' or text[i] == ':' or text[i] == '.':
                print("\n")
            i = i + 1
            while i < len(text) and text[i] == ' ':
                i = i + 1
            continue
        i = i + 1
