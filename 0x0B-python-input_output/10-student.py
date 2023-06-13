#!/usr/bin/python3
"""A module that's defined a class named Student."""


class Student:
    """a class that's represented a student."""

    def __init__(self, first_name, last_name, age):
        """Initialization of a new_Student.

        Argumnets:
            first_name (str): is the first_name of the student.
            last_name (str): is the last_name of the student.
            age (int): is the age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Getting a dict_representation of a Student.

        If attrs is a list_strings,showing only those attrs
        included in the_list.

        Arguments:
            attrs (list): (Optional) is the attributes_to_represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
