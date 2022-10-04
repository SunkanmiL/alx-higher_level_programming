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
        if id:
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
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
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
            if not list_objs:
                jfile.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                jfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns a list of the JSON representation
        Args:
            json_string (str): string representing a list of dictionaries
        """
        if not json_string or json_string == "[]":
            return []
        return json.loads(json_string)

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
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as jfile:
                list_dicts = Base.from_json_string(jfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
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
        """open a window and draw Rectangles and Squares using turtle module
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b8326c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
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
        for sq in list_squares:
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
