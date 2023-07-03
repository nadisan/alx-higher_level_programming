#!/usr/bin/python3
"""Defines the module with class Rectangle"""


class Rectangle():
    """
    Defines defines a rectangle by width and height:
    (based on 0-rectangle.py)
    """
    def __init__(self, width=0, height=0):
        """
        Creates new instance of a square.

        Args:
            width: width of the rectangle.
            height: height of the rectangle.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Retrieve width of rectangle"""
        return(Rectangle.__width)

    @width.setter
    def width(self, value):
        """
        Property setter for the width of the rectangle (1 side).

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieve height of rectangle"""
        return(Rectangle.__height)

    @height.setter
    def height(self, value):
        """
        Property setter for the height of the rectangle (1 side).

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
