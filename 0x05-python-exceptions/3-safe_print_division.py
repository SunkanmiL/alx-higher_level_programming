#!/usr/bin/python3
def safe_print_division(a, b):
    """
    divides two integers and prints the result
    Return: The value of the division,
            Otherwise None
    """
    try:
        res = a / b
    except ZeroDivisionError:
        res = None
    finally:
        print("Inside result: {}".format(res))
    return res
