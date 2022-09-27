#!/usr/bin/python3
"""
Defines a function that returns True if object is an instance of, or if the
object is an instance of a class that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if object is an instance of class, or if the object is an instance
        of a class that inherited from
    Args:
        obj (any): object type to be compared
        a_class (class): class to be compared
    Returns:
        True if object matches description
        Otherwise, False
    """

    if isinstance(obj, a_class):
        return True
    return False
