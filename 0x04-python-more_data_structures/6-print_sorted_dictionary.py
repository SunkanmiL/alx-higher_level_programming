#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    prints a dictionary by ordered keys. Assumed all keys are strings
    """
     for key, value in sorted(a_dictionary.items()):
        print("{}: {}".format(key, value))
