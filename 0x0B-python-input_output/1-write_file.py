#!/usr/bin/python3
"""Defines a function that writes a string to a text file (UTF8) and returns
the number of characters written
"""


def write_file(filename="", text=""):
    """Writes text to UTF8 file
    Args:
        filename (str): file to be written to
        text (str): text to be written
    Returns:
        number of characters written
    """
    with open(filename, encoding='utf-8', mode='w') as file:
        return file.write(text)
