#!/usr/bin/python3
def safe_print_integer(value):
    """
    prints an integer with "{:d}".format()
    Returns: True if correctly printed
                Otherwise False
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
