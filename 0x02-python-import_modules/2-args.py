#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 0:
        print("0 arguments.")
    elif len(sys.argv) == 1:
        print("{:d} argument: \n{:d}: {:s}". format(
            len(sys.argv), len(sys.argv), sys.argv[0]))
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1, end=""))
        for i in range(1, len(sys.argv)):
            print("{:d}: {:s}". format(i, sys.argv[i]))
