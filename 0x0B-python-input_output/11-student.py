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

    def to_json(self, attrs=None):
        """Retrieves dictionary representation of a Student instance"""
        if (isinstance(attrs, list) and
                all(type(ele) == str for ele in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        Args:
            json (dict): json object to be loaded
        """
        for key, val in json.items():
            setattr(self, key, val)
