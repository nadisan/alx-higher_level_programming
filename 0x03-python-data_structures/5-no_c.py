#!/usr/bin/python3
def no_c(my_string):
    i = 0
    strs = ""
    while ((len(my_string)) > i):
        if ((my_string[i] != "c") and (my_string[i] != "C")):
            strs += my_string[i]
        i += 1

    return (strs)
