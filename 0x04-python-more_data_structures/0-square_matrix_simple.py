#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        nmatrix = []
        for n in matrix:
            nmatrix.append(list(map(lambda x: x*x, n)))
        return nmatrix
