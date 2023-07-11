#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Defines a module 8-base_geometry"""


class Rectangle(BaseGeometry):
    """Defines a class  (based on 7-base_geometry.py)."""

    def __init__(self, width, height):
        """Defines Instantiation with width and height:"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
