#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    returns a new dictionary with all values multiplied by 2
    """
    return dict([(key, a_dictionary[key] * 2) for key in a_dictionary.keys()])
