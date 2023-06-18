#!/usr/bin/python3

def roman_to_int(roman_string):
    num = 0
    for k in roman_string:
        if k == "I":
            num += (1)
        if (k == "V" and (num == 0 or num > 5)):
            num += 5
        if (k == "V" and num < 5):
            num = 5 - num
        if (k == "X" and (num > 0 and num < 10)):
            num = 10 - num
        if (k == "X" and (num == 0 or num > 10)):
            num += (10)
        if k == "L":
            num += (50)
        if k == "C":
            num += (100)
        if k == "D":
            num += (500)
    return num
