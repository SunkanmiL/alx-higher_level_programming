#!/usr/bin/python3
"""
This module contains a Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes attributes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def validator(self, name, value, attr_type):
        """Validates passed arguments"""
        if type(value) is not int:
            raise TypeError(name + ' must be an integer')
        if attr_type == 1:
            if value <= 0:
                raise ValueError(name + ' must be > 0')
        if attr_type == 2:
            if value < 0:
                raise ValueError(name + ' must be >= 0')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validator("width", value, 1)
        self.__width = value

    @property
    def height(self) -> 'height':
        return self.__height

    @height.setter
    def height(self, value):
        self.validator("height", value, 1)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validator("x", value, 2)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validator("y", value, 2)
        self.__y = value

    def area(self):
        """Returns area of the Rectange instance"""
        return self.width * self.height

    def display(self):
        """Displays the rectangle using # character"""
        print(self.y * '\n', end='')
        print((((self.x * ' ' + self.width * '#') + '\n') * self.height)[:-1])

    def __str__(self):
        """Returns a readable representation of the object"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
        else:
            keys = kwargs.keys()
            if 'id' in keys:
                self.id = kwargs['id']
            if 'width' in keys:
                self.width = kwargs['width']
            if 'height' in keys:
                self.height = kwargs['height']
            if 'x' in keys:
                self.x = kwargs['x']
            if 'y' in keys:
                self.y = kwargs['y']

    def to_dictionary(self):
        """Returns dictionary representation of the instance"""
        dicti = {'x': self.x, 'y': self.y, 'id': self.id, 'height':
                 self.height, 'width': self.width}

