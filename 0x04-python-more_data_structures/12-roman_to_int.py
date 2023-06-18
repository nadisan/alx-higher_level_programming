#!/usr/bin/python3

def roman_to_int(roman_string):
    num = 0
    for k in roman_string:
        x = num % 10
        if k == "I":
            num += (1)
        elif (k == "V" and x == 0):
            num += 5
        elif (k == "V" and x == 1):
            num = num + 3
        elif (k == "X" and (x == 1)):
            num = num + 8
        elif (k == "X" and (x == 0)):
            num += (10)
        elif k == "L":
            num += (50)
        elif k == "C":
            num += (100)
        elif k == "D":
            num += (500)
    return num
