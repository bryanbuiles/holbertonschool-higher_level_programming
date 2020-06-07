#!/usr/bin/python3
"""Unittest for class Rectangle
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """unnitest
    Args:
        unittest: test for class Rectangle
    """

    def tearDown(self):
        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)

    def test_rectangle_instances(self):
        test1 = Rectangle(3, 2)
        self.assertEqual(test1.id, 1)
        self.assertEqual(test1._Base__nb_objects, 1)

        test2 = Rectangle(5, 2, 0, 0, 7)
        self.assertEqual(test2.id, 7)
        self.assertEqual(test2._Base__nb_objects, 1)

        with self.assertRaises(TypeError):
            test3 = Rectangle("bryan")
            tets4 = Rectangle(None)
            test5 = Rectangle(float("inf"))
            test6 = Rectangle(5.5, 6.6)
            test7 = Rectangle(-8, 5)
            test8 = Rectangle()

    def test_Rectangle_area(self):
        test1 = Rectangle(3, 2)
        self.assertEqual(test1.area(), 6)

        test2 = Rectangle(5, 3, 0, 1, 7)
        self.assertEqual(test2.area(), 15)

    def test_Rectangle_str(self):
        test1 = Rectangle(2, 2)
        self.assertEqual(test1.__str__(), "[Rectangle] (1) 0/0 - 2/2")

        test2 = Rectangle(3, 2, 1, 1)
        self.assertEqual(test2.__str__(), "[Rectangle] (2) 1/1 - 3/2")

        test3 = Rectangle(3, 2, 1, 1, 12)
        self.assertEqual(test3.__str__(), "[Rectangle] (12) 1/1 - 3/2")

    def test_Rectangle_update(self):
        test1 = Rectangle(2, 2)
        test1.update(6, 8)
        self.assertEqual(test1.__str__(), "[Rectangle] (6) 0/0 - 8/2")

        with self.assertRaises(ValueError):
            test1.update(**{'width': 137, 'y': -2})
            test1.update(19, None, None)

    def test_Rectangle_to_dictionary(self):
        test1 = Rectangle(2, 2)
        dir1 = {'id': 1, 'width': 2, 'height': 2, 'x': 0, 'y': 0}
        self.assertDictEqual(test1.to_dictionary(), dir1)

        test2 = Rectangle(2, 2, 7, 5, 12)
        dir2 = {'id': 12, 'width': 2, 'height': 2, 'x': 7, 'y': 5}
        self.assertDictEqual(test2.to_dictionary(), dir2)
