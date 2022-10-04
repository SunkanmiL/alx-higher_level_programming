#!/usr/bin/python3
"""This module contains a class called Base"""
import json
import csv
import turtle


class Base:
    """Base class for upcoming classes
     Attributes:
        __nb_objects (int) = number of instatiated Bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes Base with instance atrribute
        Args:
            id (int): identifier of new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation
        Args:
            list_dictionaries (list(dict)): a list of dictionaries
        Returns:
            [] - If None or empty
            Otherwise - JSOn string representation of argument
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        
        Args:
            list_objs (list(instances)): list of instances who inherits of Base
                                example: list of Rectangle or Square instances
        """
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as jfile:
            if list_objs is None:
                jfile.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                jfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns list of JSON string representation
        Args:
            json_string (str): string representing a list of dictionaries
        """
        json_list = []
        if json_string is None or len(json_string) == 0:
            return json_list
        else:
            json_list = (json.loads(json_string))
            return json_list

    @classmethod
    def create(cls, **dictionary):
        """returns an instance by processing a dictionary
        Args:
            **dictionary (dict): can be though of as double pointer to a dict
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        try:
            with open(cls.__name__ + ".json", "r") as f:
                return [cls.create(**dictionary) for
                        dictionary in cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes the CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="") as cfile:
            if not list_objs or list_objs == []:
                cfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(cfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """load from csv
        Returns:
            an empty list - if file does not exist
            otherwise - a list of instantiated classes
        """
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, "r", newline="") as cfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(cfile, fieldnames=fieldnames)
                list_dicts = [dict([key, int(val)] for key, val in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Open a window and draw Rectangles and Squares using turtle module
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b8326c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rectangle in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for square in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
