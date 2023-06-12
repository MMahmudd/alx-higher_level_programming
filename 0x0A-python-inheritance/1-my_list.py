#!/usr/bin/python3
"""Defines an class named MyList inherited list class MyList.
   A module nemd 1-my_list with class named Mylist.
"""


class MyList(list):
    """Implementemtion Class with method nemd print_sorted
    printing for the built-in list_class.
    """

    def print_sorted(self):
        """Prints a sorted list in ascending order, handling None values separately."""
        sorted_list = sorted(self, key=lambda x: x if x is not None else float('inf'))
        print(sorted_list)
