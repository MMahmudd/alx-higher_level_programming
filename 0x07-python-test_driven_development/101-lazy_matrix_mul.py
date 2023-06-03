#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""Defination of a function matrix multiplication use NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Returning the multiplying of two_matrices.

    Arguments:
        m_a (list of lists of ints/floats): The first_matrix.
        m_b (list of lists of ints/floats): The second_matrix.
    """

    return (np.matmul(m_a, m_b))
