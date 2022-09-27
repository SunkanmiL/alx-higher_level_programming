#!/usr/bin/python3
"""Defines a function to load from JSON"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file
    Args:
        filename (str): name of json file to load
    """
    with open(filename, encoding='utf-8') as file:
        return (json.loads(file.read()))
