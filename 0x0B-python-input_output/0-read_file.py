#!/usr/bin/python3
"""Defines a function that reads a text file (UTF8) and prints to stdout"""


def read_file(filename=""):
    """reads UTF8 file and prints to stdout

    Args:
        filename (str): file to be read
        """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
