#!/usr/bin/python3
""" Base.py """
import json
import csv
import turtle


class Base:
    """supper clase Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ contrutor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return json string """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation """
        with open(cls.__name__ + ".json", mode="w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                lista = [i.to_dictionary() for i in list_objs]
                f.write(cls.to_json_string(lista))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation """
        if type(json_string) != str or len(json_string) == 0:
            lista = []
            return(lista)
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        if cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return(new)

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        try:
            lista = []
            with open(cls.__name__ + ".json", mode="r", encoding="utf-8") as f:
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serialize and save in csv """
        dicc = [p.to_dictionary() for p in list_objs]
        with open(cls.__name__ + ".csv", mode="w", encoding="utf-8") as f:
            escribiendo = csv.DictWriter(f, dicc[0].keys())
            escribiendo.writeheader()
            escribiendo.writerows(dicc)

    @classmethod
    def load_from_file_csv(cls):
        """ deseriaze and load csv file """
        try:
            lista = []
            dic = {}
            with open(cls.__name__ + ".csv", mode="r", encoding="utf-8") as f:
                leyendo = csv.DictReader(f)
                for i in leyendo:
                    for k, v in dict(i).items():
                        dic[k] = int(v)
                    lista.append(cls.create(**dic))
            return (lista)
        except:
            lista = []
            return lista
