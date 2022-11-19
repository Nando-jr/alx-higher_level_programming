#!/usr/bin/python3
"""matrix_divided module"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix
    Args:
        matrix: list of lists of integers or floats
        div: number
    Returns:
           returns a new matrix
    """
    ms = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) != list or not matrix:
        raise TypeError(ms)
    a = 0
    ms = "Each row of the matrix must have the same size"
    for n in matrix:
        if type(n) != list or not n:
            raise TypeError(ms)
        if a != 0 and len(n) != a:
            raise TypeError(ms)
        for m in n:
            if type(m) != int and type(m) != float:
                raise TypeError(ms)
        a = len(n)
    rs = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return rs
