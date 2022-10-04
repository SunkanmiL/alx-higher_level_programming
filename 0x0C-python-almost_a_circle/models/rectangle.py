#!/usr/bin/python3
"""Defines a Rectangle class which inherits from Base class"""
from models.base import Base


class Rectangle(Base):
    """Defines Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes new rectangle with attributes
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): x-axis coordinate
            y (int): y-axis coordinate
            id (int): class identifier inherited from Base
        Raises:
            TypeError: if either of width, height, x or y is not an int
            ValueError: if either of width, height, x or y < 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """set/get the width of the new Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """set/get the height of the new Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """set/get the x coordinate of the new Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """set/get the y coordinate of the new Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.width * self.height

    def display(self):
        """prints in stdout the rectangle instance with
        the character '#'
        """
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for _ in range(self.y)]
        for _ in range(self.height):
            [print(" ", end="") for _ in range(self.x)]
            [print('#', end="") for _ in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """
        updates the Rectangle
        Args:
            *args (ints): new attribute values where:
                1st argument should be the id attribute
                2nd argument should be the width attribute
                3rd argument should be the height attribute
                4th argument should be the x attribute
                5th argument should be the y attribute
        """
        if args and len(args) != 0:
            cnt = 0
            for arg in args:
                if cnt == 0:
                    if not arg:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif cnt == 1:
                    self.width = arg
                elif cnt == 2:
                    self.height = arg
                elif cnt == 3:
                    self.x = arg
                elif cnt == 4:
                    self.y = arg
                cnt += 1

        elif kwargs and len(kwargs) != 0:
            for key, arg in kwargs.items():
                if key == "id":
                    if not arg:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif key == "width":
                    self.width = arg
                elif key == "height":
                    self.height = arg
                elif key == "x":
                    self.x = arg
                elif key == "y":
                    self.y = arg

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        result = f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
        result += f"{self.width}/{self.height}"
        return result
