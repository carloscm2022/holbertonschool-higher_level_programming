#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    var = []
    for i in matrix:
        var.append(list(map(lambda x: x**2, i)))
    return (var)
