#!/usr/bin/python3
""" Write the first class Base: """


class Base:
    """  """
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize class base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
