#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """ A function that used  to print x elements of a list.

    Arguments:
        my_list (list): The list to print elements from.
        x (int): represents the number of elements to be  printed.

    Return:
        Returns the real number of elements to be printed.
    """
    ret_printed_elements = 0
    for ii in range(x):
        try:
            print("{}".format(my_list[ii]), end="")
            ret_printed_elements += 1
        except IndexError:
            break
    print("")
    return (ret_printed_elements)
