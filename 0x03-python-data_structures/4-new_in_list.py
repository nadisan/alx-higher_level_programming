#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    i = 0
    if ((idx < 0) or (idx >= len(my_list))):
        return (my_list)
    else:
        newlist = my_list[:]
        newlist[idx] = element
        return (newlist)
