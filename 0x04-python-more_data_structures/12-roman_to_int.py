#!/usr/bin/python3

def roman_to_int(roman_string):
    num = 0
    for k in roman_string:
        if k == "I":
            num += (1)
        elif (k == "V" and (num == 0 or num >= 5)):
            num += 5
        elif (k == "V" and num < 5):
            num = 5 - num
        elif (k == "X" and (num > 0 and num < 10)):
            num = 10 - num
        elif (k == "X" and (num == 0 or num >= 10)):
            num += (10)
        elif k == "L":
            num += (50)
        elif k == "C":
            num += (100)
        elif k == "D":
            num += (500)
    return num
