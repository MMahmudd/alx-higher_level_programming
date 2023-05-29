#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """ A function use to execute a function safely.

    Argumets:
        fct: is function to execute.
        args: Argument of fct.

    Return:
        If errors occur - return None.
        else - return fct.
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)