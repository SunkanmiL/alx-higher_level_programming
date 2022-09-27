#!/usr/bin/python3
"""Defines Student Class"""


class Student:
    """Define a student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes Student class with attributes
        Args:
            first_name (str): first name of student
            last_name (str): last name of student
            age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary representation of a Student instance
        """
        return self.__dict__
