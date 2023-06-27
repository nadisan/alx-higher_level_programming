#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as te:
        print("Exception:", te, file=sys.stderr)
        return (None)
    return(result)