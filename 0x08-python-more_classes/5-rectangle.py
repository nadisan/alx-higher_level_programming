#!/usr/bin/python3
"""
This is a rectangle module.

The module provides a rectangle class.
"""


class Rectangle:
    """A Rectangle class with attributes width and height, and
    methods area and perimiter.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__height == 0:
            return 0
        if self.__width == 0:
            return 0
        return (2 * (self.__height + self.__width))

    def __str__(self):
        rec = ""
        for i in range(self.__height - 1):
            for i in range(self.__width):
                rec += "#"
            rec += "\n"
        for i in range(self.__width):
            rec += "#"
        return (rec)

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
