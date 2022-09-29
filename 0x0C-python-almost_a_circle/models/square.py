#!/usr/bin/python3
"""
This module contains Square class that extends Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class inherits from Rectangle class and implements a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes attributes"""
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        else:
            keys = kwargs.keys()
            if 'id' in keys:
                self.id = kwargs['id']
            if 'size' in keys:
                self.size = kwargs['size']
            if 'x' in keys:
                self.x = kwargs['x']
            if 'y' in keys:
                self.y = kwargs['y']

    def __str__(self):
        """Returns readable representation of object instance"""
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y,
                                                 self.size)

    def to_dictionary(self):
        """Returns dictionary representation of Square"""
        dicti = {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
        return dicti
