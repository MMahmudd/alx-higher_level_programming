#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Executes a function safely.

    Argumets:
        fct: The function to execute.
        args: Arguments for fct.

    Return:
        If errors occur - return None.
        else - return the result of the function,fct.
    """
    try:
        result_of = fct(*args)
        return (result_of)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
