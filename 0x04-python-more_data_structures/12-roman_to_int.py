#!/usr/bin/python3

def roman_to_int(roman_string):
    num = 0
    for k in roman_string:
        if k == "I":
            num += (1)
        x = num % 5
        if (k == "V" and x == 0):
            num += 5
        elif (k == "V" and x == 1):
            num = (num + 3)
        x = num % 10
        if (k == "X" and (x == 1)):
            num = num + 8
        elif (k == "X" and (x == 0)):
            num += (10)
        x = num % 50
        if (k == "L" and (x == 0)):
            num += (50)
        elif (k == "L" and (x != 0)):
            num += (50 - 2 * x)
        x = num % 100
        if (k == "C" and (x == 0)):
            num += (100)
        elif (k == "C" and (x != 0)):
            num += (100 - 2 * x)
        x = num % 500
        if (k == "D" and (x == 0)):
            num += (500)
        elif (k == "D" and (x != 0)):
            num += (500 - 2 * x)
    return num
