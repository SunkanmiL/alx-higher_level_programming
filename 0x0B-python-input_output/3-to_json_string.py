#!/usr/bin/python3
"""Defines a function to convert string to JSON"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object(string)
    Args:
        my_obj (any): object to be converted to JSON
    Returns:
        A JSON format text
    """
    return json.dumps(my_obj)
