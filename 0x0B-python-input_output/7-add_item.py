#!/usr/bin/python3
"""Defines the function 7-add_item"""

import os.path
import sys
"""Imports sys module"""
from sys import argv
import json
"""Imports json module"""

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
my_list = []

if os.path.exists(filename):
    my_list = load_from_json_file(filename)

for i in argv[1:]:
    my_list.append(index)

save_to_json_file(my_list, filename)
