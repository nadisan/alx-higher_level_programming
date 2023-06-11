#!/usr/bin/python3

import hidden_4
if __name__ != "__main__":
    exit()
i = 0
while ((len(dir(hidden_4))) - i):
    if(dir(hidden_4)[i][0] != "_"):
        print("{}".format(dir(hidden_4)[i]))
    i = i + 1
