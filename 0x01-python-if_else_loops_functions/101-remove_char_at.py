#!/usr/bin/python3
def remove_char_at(str, n):
    str1 = ""
    for i in range(len(str)):
        if i == n:
            continue
        str1 += str[i]
    return (str1)
