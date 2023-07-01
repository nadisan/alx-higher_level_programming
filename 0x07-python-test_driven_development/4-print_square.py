#!/usr/bin/python3
"""Defines function [print_square"""


def print_square(size):
    """
    defines a function that prints a square with the character #

    args:
        int size: length of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
