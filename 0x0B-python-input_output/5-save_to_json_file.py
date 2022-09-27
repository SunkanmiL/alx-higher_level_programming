#!/usr/bin/python3
"""Defines a function that writes a object to a text file using JSON
representation"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file
    Args:
        my_obj (any): object to be written to file
        filename (str): name of file to be written to
    """
    with open(filename, mode='w') as file:
        json.dump(my_obj, file)
