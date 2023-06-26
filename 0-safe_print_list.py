#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    if (x > len(my_list)):
        x = len(my_list)
    for i in range(x):
        if (my_list[i]):
            print("{:}".format(my_list[i]))
        else:
            break
    return (x)
