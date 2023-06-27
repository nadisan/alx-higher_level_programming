#!/usr/bin/python3
"""Defines class a square"""


class Square():
    """
    Class that defines properties of a square by: (based on 4-square.py)

    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size=0):
        """
        Creates new instance of a square.

        Args:
            size: size of the square (1 side).
        """
        self.__size = size

    def area(self):
        """
        Calculates the area of a square.

        Returns the current square area
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """Retrieve size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Property setter for the size of the square (1 side).

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        for i in range (self.__size):
            for i in range (self.__size):
                print("#", end="")
            print()
