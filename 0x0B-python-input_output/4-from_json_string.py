#!/usr/bin/python3
"""Defines the function from_json_string"""

import json
"""Imports json module"""


def from_json_string(my_str):
    """Defines the function that returns an object (Python data structure)
    represented by a JSON string:"""
    return json.dumps(my_str)
