#!/usr/bin/python3
def best_score(a_dictionary):
    """
    returns a key with the biggest integer value.
    """
    if a_dictionary:
        max_key = None
        max_value = float('-inf')
        for key in a_dictionary.keys():
            if a_dictionary[key] > max_value:
                max_value = a_dictionary[key]
                max_key = key
        return max_key
    return None
