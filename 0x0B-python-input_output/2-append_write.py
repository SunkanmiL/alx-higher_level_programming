#!/usr/bin/python3
"""Defines a function that appends a string to a text file (UTF8) and returns
the number of characters written
"""


def append_write(filename="", text=""):
    """Appends text to UTF8 file
    Args:
        filename (str): file to be appended to
        text (str): text to be appended
    Returns:
        number of characters added
    """
    with open(filename, encoding='utf-8', mode='a') as file:
        return file.write(text)
