#!/usr/bin/python3
"""Defines lookup function"""


def lookup(obj):
    """
    Defines a funuction that
    returns the list of available attributes and methods of an object:
    arg:
        obj: object to look up
    Return: a list object.
    """
    return dir(obj)
