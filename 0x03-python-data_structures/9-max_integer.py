#!/usr/bin/python3

def max_integer(my_list=[]):
    i = 0
    length = len(my_list)
    if i == length:
        return (None)
    else:
        a = my_list[0]
        while (i < length):
            if (a < my_list[i]):
                a = my_list[i]
            i += 1
    return (a)
