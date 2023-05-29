#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """a function that used to Print an integer with "{:d}".format().

    If the ValueError exception is caught, the corresponding error message
    is printed to the standard error output.

    Arguments:
        value (int): An integer to be printed.

    Return:
        If TypeErrors occur - return False.
        else return - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
