#!/usr/bin/python3
"""Defines function that checks an inheritance of the specified class"""


def inherits_from(obj, a_class):
    """
    Defines  is an instance of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False.
    """
    return (False if (type(obj) is a_class) else isinstance(obj, a_class))
