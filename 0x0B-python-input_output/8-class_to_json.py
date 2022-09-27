#!/usr/bin/python3
"""defines a function to return dictionary description
with simple data structure for JSON serilaization of an object
"""


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for
    JSON serialization of an object

    Args:
        obj (object): The object inputted to create a class
    """
    return obj.__dict__
