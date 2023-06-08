#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""Definition of a function matrix multiplication use NumPy."""
import numpy as my_numpy


def lazy_matrix_mul(m_a, m_b):
    """Returning the multiplying of two_matrices.

    Arguments:
        m_a (list of lists of ints/floats): The first_matrix.
        m_b (list of lists of ints/floats): The second_matrix.
    """
    if len(m_a[0]) != len(m_b):
        raise ValueError("Matrix dimensions are incompatible for multiplication.")
    return (my_numpy.matmul(m_a, m_b))
