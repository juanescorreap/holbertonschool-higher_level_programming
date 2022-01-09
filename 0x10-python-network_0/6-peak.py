#!/usr/bin/python3

"""Function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Function that finds a peak in a list of unsorted integers"""
    n = len(list_of_integers)
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if (mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and (mid == n-1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return mid
        if mid == 0 or list_of_integers[mid - 1] > list_of_integers[mid]:
            right = mid -1
        else:
            left = mid + 1
            
