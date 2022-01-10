#!/usr/bin/python3

"""Function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Function that finds a peak in a list of unsorted integers"""

    if list_of_integers is None or len(list_of_integers) < 1:
        return None
    maximum = max(list_of_integers)
    return maximum
