#!/usr/bin/python3
"""Defines function that checks an instance of the specified class"""


def is_same_class(obj, a_class):
    """
    Defines checks if instance is specified class
    """
    return (type(obj) is a_class)
