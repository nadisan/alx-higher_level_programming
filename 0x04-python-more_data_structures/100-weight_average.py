#!/usr/bin/python3

def weight_average(my_list=[]):
    if (my_list is None):
        return 0
    x = 0
    y = 0
    for s, v in my_list:
        x += (s*v)
        y += v
    return (x/y)
