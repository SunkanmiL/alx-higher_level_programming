#!/usr/bin/python3


def safe_print_integer_err(value):
    """
    prints an integer followed by a new line
    Return: True if value is correctly printed,
            otherwise False and prints in stderr the error precede by Exception
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
