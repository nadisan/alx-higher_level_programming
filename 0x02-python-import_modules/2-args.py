#!/usr/bin/python3

import sys

if __name__ != "__main__":
    exit()

if len(sys.argv) >= 2:
    if len(sys.argv) == 2:
        print("1 argument: {}".format(sys.argv[1]))
    else:
        i = 1
        while (i < len(sys.argv)):
            print("{} arguments: {}".format(i, sys.argv[i]))
            i += 1
else:
    print(".")
