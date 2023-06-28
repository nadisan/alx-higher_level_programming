#!/usr/bin/python3
"""Defines class a square"""


class Square():
    """
    Class that defines properties of a square by: (based on 4-square.py)

    Attributes:
        size: size of a square (1 side).
    """
    position = 0

    def __init__(self, size=0, position=(0, 0)):
        """
        Creates new instance of a square.

        Args:
            size: size of the square (1 side).
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Retrives position of square print"""
        return (self.position)

    @position.setter
    def position(self, value):
        """
        Propety setter for the position of square

        Raises:
            TypeError: position must be a tuple of 2 positive integers
        """
        if ((type(value) is not tuple) or (len(value) != 2)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif((type(value[1]) is not int or (type(value[0]) is not int))
        elif (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        x = value[0]
        y = value[1]

    def my_print(self):
        """
        prints in stdout the square area with the character #
        """
        (x, y) = self.__position
        if self.__size == 0 and (x, y) == (0, 0):
            print()
            return
        for i in range(y + self.__size):
            for i in range(x + self.__size):
                if (i < x):
                    print(end=" ")
                else:
                    print("#", end="")
            print()
