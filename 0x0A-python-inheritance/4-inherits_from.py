#!/usr/bin/python3
"""
Defines a function that returns True if object is an instance of a class that
inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Checks if object is an instance of class, or if the object is an instance\
        of a class that inherited from
    Args:
        obj (any): object type to be compared
        a_class (class): class to be compared
    Returns:
        True if object matches description
        Otherwise, False
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
