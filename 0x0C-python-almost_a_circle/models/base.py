#!/usr/bin/python3
'''Module for Base class.'''
import json
import os.path
import sys


class Base:
    '''A representation of the base of our OOP hierarchy.'''

    __nb_objects = 0

    def __init__(self, id=None):
        """initialize class base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save_to_file definition """

        filename = "{:s}.json".format(cls.__name__)
        objs = []

        if list_objs is not None:
            for i in range(len(list_objs)):
                objs.append(cls.to_dictionary(list_objs[i]))

        with open(filename, mode="w", encoding="utf-8") as a_file:
            a_file.write(cls.to_json_string(objs))

    @staticmethod
    def from_json_string(json_string):
        """
        Defines a function  that returns the list of the JSON string
        representation json_string
        """
        listt = []

        if json_string is not None and len(json_string) != "":
            listt = json.loads(json_string)
        return listt

    @classmethod
    def create(cls, **dictionary):
        """Update the class Base by adding class
        returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """list of instance"""
        filename = "{:s}.json".format(cls.__name__)
        new_list = []

        if os.path.exists(filename):
            with open(filename, mode="r", encoding="utf-8") as a_file:
                contentstr = a_file.read()
            a_list = cls.from_json_string(contentstr)
            for i in range(len(a_list)):
                new_list.append(cls.create(**a_list[i]))

        return (new_list)
