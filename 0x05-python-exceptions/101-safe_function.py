#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """ A function executes safely.

    Argumets:
        fct:  function.
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
