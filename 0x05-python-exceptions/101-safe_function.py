import sys

def safe_function(fct, *args):
    try:
        result_of = fct(*args)
        return result_of
    except Exception as e:
        error_message = "Exception: {}".format(e)
        print(error_message, file=sys.stderr)
        return None
