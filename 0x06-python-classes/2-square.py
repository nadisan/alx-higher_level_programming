#!/usr/bin/python3
"""Defines a class square"""


class Square():
    """
    Class that defines properties of square by: based on 1-square

    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size=0):
        """
        Creates new instances of square.

        Args:
            size: size of the square (1 side).
        """
        self.__size = size
        if type(size) is not int:
            raise ValueError("size must be >= 0")
        elif size < 0:
            raise TypeError("size must be an integer")
        else:
            self.__size = size
