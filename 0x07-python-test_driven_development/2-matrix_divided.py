#!/usr/bin/python3
# 2-matrix_divided.py
"""Defination of a func a matrix_ division."""


def matrix_divided(matrix, div):
    """Dividing all_elements of matrix.

    Argumnets:
        matrix (list): A list of lists of inegers_or_floats.
        div (int/float): divisor.
    Rais:
        TypeError: If the matrix has contained non numbers.
        TypeError: If the matrix have contained rows of different_sizes.
        TypeError: If div is not an integer_or_float.
        ZeroDivisionError: If div is zero.
    Return:
        A new_matrix represents the result of the_division.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
