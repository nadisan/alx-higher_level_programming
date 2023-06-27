#!/usr/bin/python3
"""Defines class a square"""


class Square():
    """
    Class that defines properties of a square by: (based on 2-square.py)

    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size=0):
        """
        Creates new instance of a square.

        Args:
            size: size of the square (1 side).
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates the area of a square.

        Returns the current square area
        """
        return (self.__size * self.__size)
