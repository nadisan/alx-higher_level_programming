#!/usr/bin/python3
"""Defines class for student creation"""


class Student:
    """class with  student object"""
    def __init__(self, first_name, last_name, age):
        """initiate  student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student"""
        new = {}
        i = 0
        count = 0
        if type(attrs) is list:
            for key in attrs:
                if key in self.__dict__:
                    new[key] = self.__dict__[key]
            return new
        return self.__dict__
