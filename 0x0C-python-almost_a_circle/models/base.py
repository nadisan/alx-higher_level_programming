#!/usr/bin/python3
""" Write the first class Base: """
import json
""" impots json"""


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
