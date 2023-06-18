#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    def mul(n):
        return n * number

    # Multiply all numbers by number
    result = map(mul, my_list)
    return (list(result))
