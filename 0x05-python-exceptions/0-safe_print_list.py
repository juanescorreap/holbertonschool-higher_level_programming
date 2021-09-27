#!/usr/bin/python3y
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for i in my_list[:x]:
            print("{}".format(i), end="")
        print()
    except:
        return(i)
    return(i)
