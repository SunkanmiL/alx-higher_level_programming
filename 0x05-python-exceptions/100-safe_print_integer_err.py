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
    except (TypeError, ValueError) as e:
        import sys
        print("Exception: {}".format(e), file=sys.stderr)
        return False
