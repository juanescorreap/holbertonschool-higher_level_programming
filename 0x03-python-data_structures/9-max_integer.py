#!/usr/bin/python3
import builtins


def max_integer(my_list=[]):
    biggest = my_list[0]
    if my_list:
        for i in my_list:
            if biggest < i:
                    biggest = i
        return(biggest)
    else:
        return(None)
