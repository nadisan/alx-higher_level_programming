#!/usr/bin/python3
"""Defines a class MyList that inherits from list"""


class MyList(list):
    """class with method print_sorted list"""
    pass

    def print_sorted(self):
        """Defines a class MyList that inherits from list

        args:
            self: list that is inherited
        prints: sorted list
        """ 
        print(sorted(list(self)))
