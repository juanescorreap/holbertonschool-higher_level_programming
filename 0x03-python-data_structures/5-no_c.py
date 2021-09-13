#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string.copy()
    i = 0
    while (i < len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            new_string = my_string[:i] + my_string[i+1:]
        i = i + 1
    return(new_string)
