#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 97 <= ord(i) and 122 >= ord(i):
            print(chr(ord(i)-32), end="")
        else:
            print(i, end="")
    print("")
