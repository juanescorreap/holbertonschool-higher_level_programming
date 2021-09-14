#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dictionary = {}
    for i in sorted(a_dictionary):
        sorted_dictionary[i] = a_dictionary[i]
    print(sorted_dictionary)
