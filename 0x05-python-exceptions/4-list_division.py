#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """ A function that used to divide element by element 2 lists.

    Arguments:
        my_list_1 (list): First list_elements.
        my_list_2 (list): Second list_elements.
        list_length (int):A number of an element to divide.

    Return:
        Return a new list( list_length )containing with all the divisions.
    """
    new_list_all = []
    for ii in range(0, list_length):
        try:
            division_num = my_list_1[ii] / my_list_2[ii]
        except TypeError:
            print("wrong type")
            division_num = 0
        except ZeroDivisionError:
            print("division by 0")
            division_num = 0
        except IndexError:
            print("out of range")
            division_num = 0
        finally:
            new_list_all.append(division_num)
    return (new_list_all)
