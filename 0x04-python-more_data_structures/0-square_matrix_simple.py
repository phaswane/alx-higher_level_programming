#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    _matrix = []
    for row in matrix:
        _matrix.append([number ** 2 for number in row])
    return _matrix
