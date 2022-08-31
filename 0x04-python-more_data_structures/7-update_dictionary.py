#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    replaces or adds key/value in a dictionary and returns a new copy
    """
    a_dictionary[key] = value
    return a_dictionary
