#!/usr/bin/python3
"""Defines an empty class BaseGeometry"""


class BaseGeometry:
    """Defines an empty class BaseGeometry"""

    def area(self):
        """Raises an Exception with the message area() is not implemented"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value
        Args:
            name (str): name of the parameter
            value (int): parameter to validate
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if type(value) != int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
