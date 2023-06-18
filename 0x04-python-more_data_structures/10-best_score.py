#!/usr/bin/python3

def best_score(a_dictionary):
    best = "None"
    H = 0
    if (a_dictionary):
        for k in a_dictionary:
            if a_dictionary[k] >= H:
                H = a_dictionary[k]
                best = k
    return best
