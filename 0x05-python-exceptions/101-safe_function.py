#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    try:
        result_of = fct(*args)
        return result_of
    except Exception as er:
        error_messages = "Exception: {}".format(er)
        print(error_messages, file=sys.stderr)
        return None
