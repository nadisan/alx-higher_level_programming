#!/usr/bin/python3
""" square """
from models.rectangle import Rectangle
"""superclass Rectangle"""


class Square(Rectangle):
    """ class Square that inherits from Rectangle  """
    def __init__(self, size, x=0, y=0, id=None):
         """initialize instance attributes"""
         super().__init__(size, size, x, y, id)
         self.width = size
         self.height = size

    def __str__(self):
        """defines what string return"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
                type(self).__name__, self.id, self.x,
                self.y, self.width)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updater of elements of self"""
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                    self.height = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        elif kwargs is not None and len(kwargs) != 0:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "size":
                    self.width = kwargs[key]
                    self.height = kwargs[key]
                elif key == "x":
                    self.x = kwargs[key]
                elif key == "y":
                    self.y = kwargs[key]

    def to_dictionary(self):
        """ define dictionary representation of a square """
        dic = {'id':0,'x': 0, 'size': 0, 'y':0}
        for i in dic:
            if i == "x":
                dic[i] = self.x
            if i == "y":
                dic[i] = self.y
            if i == "id":
                dic[i] = self.id
            if i == "size":
                dic[i] = self.size
        return dic
