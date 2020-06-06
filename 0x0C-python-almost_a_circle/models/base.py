#!/usr/bin/python3
""" Base.py """
import json


class Base:
    """supper clase Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        with open(cls.__name__ + ".json", mode="w", encoding="UTF-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                lista = [i.to_dictionary() for i in list_objs]
                f.write(cls.to_json_string(lista))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            lista = []
            return(lista)
        else:
            return json.loads(json_string)
