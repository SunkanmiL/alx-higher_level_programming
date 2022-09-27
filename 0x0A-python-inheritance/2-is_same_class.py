#!/usr/bin/python3
"""
Defines a function that returns True if object is exactly an instance of the
specified class
"""


def is_same_class(obj, a_class):
    """
    Checks if two objects are the same class
    Args:
        obj (any): object type to be compared
        a_class (class): class to be compared
    Returns:
        True if the object is exactly an instance of the specified class
        Otherwise, False
    """

    if type(obj) == a_class:
        return True
    return False
