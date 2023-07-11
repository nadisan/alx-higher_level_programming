#!/usr/bin/python3
"""Defines an empty class BaseGeometry"""


class BaseGeometry:
    """Defines an empty class  (based on 6-base_geometry.py)."""

    def area(self):
        """Defines a function that raises area error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Defines a function that validates value is int and >0"""
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
