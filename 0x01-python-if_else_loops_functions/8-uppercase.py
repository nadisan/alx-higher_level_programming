#!/usr/bin/python3
def uppercase(str):
    str1 = ""
    for i in range(len(str)):
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            j = (ord(str[i]) - 32)
            str1 += chr(j)
            continue
        str1 += str[i]
    print(str1)
