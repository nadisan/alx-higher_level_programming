#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    n_dictionary = {}
    for k in a_dictionary:
        n_dictionary[k] = 2 * a_dictionary[k]
    return n_dictionary
