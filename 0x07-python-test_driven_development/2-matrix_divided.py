#!/usr/bin/python3
"""Defines a function matrix_divided(matrix, div)"""


def matrix_divided(matrix, div):
    """
    Defines a function that divides all elements of a matrix

    args:
        matrix: must be a list of lists of integers or floats,
                Each row of the matrix must be of the same size.
        div: must be a number (integer or float),
             can’t be equal to 0.
    """
    newm = []
    if (type(div) is not int):
        if (type(div) is not float):
            raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    rowl = len(matrix[0])
    for i in range(len(matrix)):
        if (rowl != len(matrix[i])):
            raise TypeError("Each row of the matrix must have the same size")
        else:
            newm.append([])
            for j in range(rowl):
                num = round(((matrix[i][j]) / div), 2)
                newm[i].append(num)
    return (newm)
