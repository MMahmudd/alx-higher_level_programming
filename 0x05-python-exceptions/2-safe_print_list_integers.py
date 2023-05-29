#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x integers from a list.

    Arguments:
        my_list (list): The list to be printed an element of.
        x (int): The numbr of elements of my_list to be printed.

    Return:
        The real numbers of an element to be printed.
    """
    ret_printed_elements = 0
    for ii in range(0, x):
        try:
            print("{:d}".format(my_list[ii]), end="")
            ret_printed_elements += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret_printed_elements)
