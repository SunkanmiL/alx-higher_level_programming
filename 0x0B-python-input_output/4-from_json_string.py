#!/usr/bin/python3
"""Defines a function to write an Object to a text file, using a JSON
representation"""
import json


def from_json_string(my_str):
    """returns the Python representation of a JSON string

    Args:
        my_str (str): object to be converted to JSON
    Returns:
        A Python object from json
     """
    return json.loads(my_str)
