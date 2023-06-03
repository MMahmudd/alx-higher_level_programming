#!/usr/bin/python3
"""a module used to findout the max_integer in a list.
"""


def max_integer(list=[]):
    """a function to find & return the max_integer in the list of integer
    If a list is empty,the function will return None
    """
    if len(list) == 0:
        return None
    result_of = list[0]
    ii = 1
    while ii < len(list):
        if list[ii] > result_of:
            result_of = list[ii]
        ii += 1
    return result_of

