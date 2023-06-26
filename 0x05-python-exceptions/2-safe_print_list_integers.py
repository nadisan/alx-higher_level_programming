#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    j = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except IndexError:
            raise
        except Exception as e:
            pass
        else:
            j += 1
    print()
    return (j)
