#!/usr/bin/python3
"""Defines a Square class which is a subclass of Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a Square class"""

    def __init__(self, size):
        """Initialises the square class
        Args:
            size (int): length of the square sides
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
