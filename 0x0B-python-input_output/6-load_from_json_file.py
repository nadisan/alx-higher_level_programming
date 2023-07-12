#!/usr/bin/python3
"""Defines the function load_from_json_file"""

import json
"""Imports json module"""


def load_from_json_file(filename):
    """Defines the function that writes an Object to a text file,
    using a JSON representation"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
