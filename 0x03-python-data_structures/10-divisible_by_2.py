#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    i = 0
    div2 = []
    while (i < len(my_list)):
        if ((my_list[i] % 2) == 0):
            div2 += [True]
        else:
            div2 += [False]
        i += 1
    return div2
