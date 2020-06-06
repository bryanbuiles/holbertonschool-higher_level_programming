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
        if type(json_string) != str or len(json_string) == 0:
            lista = []
            return(lista)
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        if cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return(new)

    @classmethod
    def load_from_file(cls):
        try:
            lista = []
            with open(cls.__name__ + ".json", mode="r", encoding="UTF-8") as f:
                file = f.read()
            text = cls.from_json_string(file)
            for i in text:
                if type(i) == dict:
                    lista.append(cls.create(**i))
                else:
                    lista.append(i)
            return (lista)
        except:
            lista = []
            return lista
