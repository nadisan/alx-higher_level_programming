#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    del_dic = []
    for k in a_dictionary:
        if a_dictionary[k] == value:
            del_dic += [k]
    for k in del_dic:
        del a_dictionary[k]
    return a_dictionary
