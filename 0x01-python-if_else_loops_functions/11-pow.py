#!/usr/bin/python3
def pow(a, b):
    power = 1
    if b > 0:
        for i in range(b):
            power = power * a
    else:
        b = b * -1
        for i in range(b):
            power = power / a
    return power
