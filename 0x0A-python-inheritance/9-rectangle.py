#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a new Rectangle
        Args:
            width (int): width of the new Rectangle
            height (int): height of the new Rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle
        Returns:
           The area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        str funtion for rectangle
        Returns:
            [Rectangle] <width>/<height>
        """

        result = '[' + str(self.__class__.__name__) + '] '
        result += str(self.__width) + '/' + str(self.__height)
        return result
