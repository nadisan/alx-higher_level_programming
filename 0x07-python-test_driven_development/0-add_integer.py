#!/usr/bin/python3
"""
Defines a function add_integer(a, b=98)
"""


def add_integer(a, b=98):
    """
    Defines a function that takes and adds two integers
    
    args:
        int a: must be integer
        int b: must be integer, assigned value 98 at fun def
    """
    if (type(a) is not int):
        if (type(a) is not float):
            raise TypeError("a must be an integer")
    elif type(b) is not int:
        if (type(b) is not int):
            raise TypeError("b must be an integer")
    return int(a + b)



