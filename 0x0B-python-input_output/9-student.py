#!/usr/bin/python3
"""A module that's defined a clas named Student"""


class Student:
    """
    A class that's defined a function of student.

    Attribute:
        first_name (str): is first_name of student.
        last_name (int): is last_name of student.
        age (int): is an age of student.
    """
    def __init__(self, first_name, last_name, age):
        """Creating new_instances of Student.

        Argumnets:
            first_name (str): is first_name of student.
            last_name (int): is last_name of student.
            age (int): is an age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dict_representation of a Student_nstance.

        Return:
            dict: is dictionary_representation.
        """
        return self.__dict__
