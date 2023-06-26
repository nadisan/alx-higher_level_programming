#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    j = 0
    for i in range(x):
        try:
            print("{:}".format(my_list[i]), end="")
        except Exception as e:
            break
        else:
            j += 1
    print(end="\n")
    return (j)
