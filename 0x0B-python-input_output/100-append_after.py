#!/usr/bin/python3
"""Defines append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing
    a specific string
    Args:
        filename (str): name of file to be appended to
        search_string (str): starting point of append operation
        new_string (str): string to be appended
    """
    text = ""
    with open(filename) as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, mode='w') as w:
        w.write(text)
