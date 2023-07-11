#!/usr/bin/python3
import json
"""Defines the function write_file"""


def to_json_string(my_obj):
    """Defines  a function returning JSON representation of an object
    with open('basic.json', mode='w', encoding='utf-8') as f:"""
    return json.dumps(my_obj)
