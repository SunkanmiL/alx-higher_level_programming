#!/usr/bin/python3
def print_last_digit(number):
    digit = abs(number) % 10
    if digit < 10:
        print("{}".format(digit), end="")
        return digit
    else:
        print_last_digit(digit)
