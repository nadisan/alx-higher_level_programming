#!/usr/bin/python3
"""Defines a function text_indentation"""


def text_indentation(text):
    """
    Defines a function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    args:
        text: must be a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        if ((i == ".") or (i == "?") or (i == ":")):
            print("\n")
        else:
            print("{}".format(i), end="")
