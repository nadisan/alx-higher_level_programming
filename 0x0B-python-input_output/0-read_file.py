#!/usr/bin/python3
"""Defines function read_file"""


def read_file(filename=""):
    """Defines a function that reads a text file (UTF8)
    and prints it to stdout:"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
