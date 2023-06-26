#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        j = a/b
    except (ZeroDivisionError):
        j = None
    finally:
        print("Inside result: {}".format(j))
    return (j)
