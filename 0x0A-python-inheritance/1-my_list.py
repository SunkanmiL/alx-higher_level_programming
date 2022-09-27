#!/usr/bin/python3
"""Defines a class MyList that inherits from list"""


class MyList(list):
    """Class MyList that inherits from list"""

    def print_sorted(self):
        """Public instance method that prints sorted list (ascending sort)"""
        print(sorted(self))
