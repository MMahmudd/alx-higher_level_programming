#!/usr/bin/python3
"""A module that's defined a class Pascal's_Triangle."""


def pascal_triangle(n):
    """A function Represented Pascal's Triangle of size n.

    Return a list of lists of ints represented the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        trii = triangle[-1]
        tmpp = [1]
        for ii in range(len(trii) - 1):
            tmpp.append(trii[ii] + trii[ii + 1])
        tmpp.append(1)
        triangle.append(tmpp)
    return triangle
