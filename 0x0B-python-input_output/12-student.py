#!/usr/bin/python3
""" class student """


class Student:
    """ student data
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ return jason dict """
        if type(attrs) != list or attrs is None:
            return self.__dict__
        else:
            dic = {}
            for i in attrs:
                if type(i) != str:
                    return (self.__dict__)
                if i in self.__dict__:
                    dic[i] = self.__dict__[i]
            return (dic)
