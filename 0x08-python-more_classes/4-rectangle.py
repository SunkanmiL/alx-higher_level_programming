#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Represent a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle
        Args:
            width (int): The width of the new rectangle
            height (int): The height of the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle
        Returns:
            width (int): The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle
        Returns:
            height (int): The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.height * 2)

    def __str__(self):
        """Return a printable representation of the rectangle
        Represents the rectangle with the # character
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        res = []
        for i in range(self.__height):
            [res.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                res.append("\n")
        return "".join(res)

    def __repr__(self):
        """Return the string representation of the rectangle"""
        res = "Rectangle(" + str(self.__width)
        res += ", " + str(self.__height) + ")"
        return res
