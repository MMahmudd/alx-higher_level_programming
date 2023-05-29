#!/usr/bin/python3


def safe_print_integer(value):
    """A function that Print an integer with "{:d}".format().

    Arguments:
        value (int): The integers to be printed.

    Return:
        If TypeErrores or ValueErrores occur - False.
        else - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
