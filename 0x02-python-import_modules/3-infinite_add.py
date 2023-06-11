#!/usr/bin/python3

import sys

if __name__ != "__main__":
    exit()

i = 1
sums = 0

while (i < (len(sys.argv))):
    sums = sums + int(sys.argv[i])
    i = i + 1
print("{}".format(sums))
