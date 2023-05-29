#!/usr/bin/python3

def safe_print_division(a, b):
    """Returning the division_numbers of a/b."""
    try:
        division_num = a / b
    except (TypeError, ZeroDivisionError):
        division_num = None
    finally:
        print("Inside result: {}".format(division_num))
    return (division_num)
