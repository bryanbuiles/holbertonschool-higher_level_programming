#!/usr/bin/python3
""" Object Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square ihnertes Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        Rectangle.__init__(self, width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".
                format(self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """ update square atributtes """
        if len(kwargs) <= 0 and len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        dic = {}
        dic["id"] = self.id
        dic["size"] = self.size
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
