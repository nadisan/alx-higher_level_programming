#!/usr/bin/python3

import sys

if __name__ != "__main__":
    exit()

if len(sys.argv) >= 2:
    if len(sys.argv) == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(len(sys.argv) -1))
        i = 1
        while (i < len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
else:
    print("0 arguments.")
