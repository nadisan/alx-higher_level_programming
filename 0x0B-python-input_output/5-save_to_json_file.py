#!/usr/bin/python3
"""Defines the function save_to_json_file"""

import json
"""Imports json module"""


def save_to_json_file(my_obj, filename):
    """Defines the function that writes an Object to a text file,
    using a JSON representation"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
