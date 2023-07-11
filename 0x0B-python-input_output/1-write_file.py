#!/usr/bin/python3
"""Defines the function write_file"""


def write_file(filename="", text=""):
    """Defines a function that writes a string to a text file (UTF8)
    and returns the number of characters written"""
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
