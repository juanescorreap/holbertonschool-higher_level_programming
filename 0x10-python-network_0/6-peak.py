#!/usr/bin/python3

"""Function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """ retuns a peak number from a unsorted list"""
    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    list_of_integers.sort(reverse=True)
    return list_of_integers[0]
