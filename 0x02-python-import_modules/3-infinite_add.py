#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    import sys
    sum = 0
    for i in range(1, len(sys.argv)):
        sum = sum + int(sys.argv[i])
    print("{:d}".format(sum))
