#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    i = 0
    j = 0

    
    for i in range(len(matrix)):
        row = matrix[i]
        while (j < (len(row))):
            print("{:d}".format(row[j]), end=" ")
            j += 1
        print()
        j = 0


