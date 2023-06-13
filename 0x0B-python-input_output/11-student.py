#!/usr/bin/python3
"""A madule that's defined a class named Student."""


class Student:
    """A class that's represented a student."""

    def __init__(self, first_name, last_name, age):
        """Initialization of a new_Student.

        Argumnets:
            first_name (str): is the first_name of the student.
            last_name (str): is last_name of the student.
            age (int): is the age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Getting a dict that's represented the Student.

        If attrs is a list_of_strings, showing
        only those_attributes including in the list.

        Argumnets:
            attrs (list): (Optional) is the attributes to_represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {kk: getattr(self, kk) for kk in attrs if hasattr(self, kk)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replacing all_attributes of the_Student.

        Argumnets:
            json (dict): is the key/value_pairs to replacing attrs with.
        """
        for kk, vv in json.items():
            setattr(self, kk, vv)
