#!/usr/bin/python3
"""Defines an class named MyList inherited list class MyList.
   A module nemd 1-my_list with class named Mylist.
"""


class MyList(list):
    """Implementemtion Class with method nemd print_sorted
    printing for the built-in list_class.
    """

    def print_sorted(self):
        """Printing a list sort ascending_order."""
        print(sorted(self))
