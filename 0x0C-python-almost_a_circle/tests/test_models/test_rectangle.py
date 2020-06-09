#!/usr/bin/python3
"""Unittest for class Rectangle
"""
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """unnitest
    Args:
        unittest: test for class Rectangle
    """

    def tearDown(self):
        """ tear module unnitest """
        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)

    def test_rectangle_instances(self):
        """ test for rectnagle instances """
        test1 = Rectangle(3, 2)
        self.assertEqual(test1.id, 1)
        self.assertEqual(test1._Base__nb_objects, 1)

        test2 = Rectangle(5, 2, 0, 0, 7)
        self.assertEqual(test2.id, 7)
        self.assertEqual(test2._Base__nb_objects, 1)

    def test_rectangle_raises_errors(self):
        """ test for rectangle_raises_errors """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            test3 = Rectangle("bryan", 1)
        with self.assertRaises(TypeError):
            test18 = Rectangle(1)
        with self.assertRaises(TypeError):
            tets4 = Rectangle(None, 1)
        with self.assertRaises(TypeError):
            test5 = Rectangle(float("inf"), 1)
        with self.assertRaises(TypeError):
            test6 = Rectangle(5.5, 6.6)
        with self.assertRaises(TypeError):
            test8 = Rectangle()
        with self.assertRaises(TypeError):
            test9 = Rectangle(["hello"], 1)
        with self.assertRaises(TypeError):
            test10 = Rectangle({"hello": "bryan"}, 1)
        with self.assertRaises(TypeError):
            test11 = Rectangle((1, 1), 1)
        with self.assertRaises(TypeError):
            test12 = Rectangle((1, 1, 1), 1)
        with self.assertRaises(TypeError):
            test17 = Rectangle(float('nan'), 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            test23 = Rectangle(2, "bryan")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            test24 = Rectangle(2, 3, "bryan")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            test25 = Rectangle(2, 3, 5, "bryan")

        with self.assertRaises(ValueError):
            test13 = Rectangle(5, 2, -1)
        with self.assertRaises(ValueError):
            tets14 = Rectangle(5, 2, 1, -1)
        with self.assertRaises(ValueError):
            test15 = Rectangle(5, -8)
        with self.assertRaises(ValueError):
            test16 = Rectangle(-8, 5)
        with self.assertRaisesRegex(ValueError, "width must be >= 0"):
            test19 = Rectangle(-8, 4)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            test20 = Rectangle(5, 2, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            tets21 = Rectangle(5, 2, 1, -1)
        with self.assertRaisesRegex(ValueError, "height must be >= 0"):
            test22 = Rectangle(5, -8)

    def test_Rectangle_area(self):
        """ test for Rectangle_area """
        test1 = Rectangle(3, 2)
        self.assertEqual(test1.area(), 6)

        test2 = Rectangle(5, 3, 0, 1, 7)
        self.assertEqual(test2.area(), 15)

    def test_Rectangle_str(self):
        """ test for test_Rectangle_str """
        test1 = Rectangle(2, 2)
        self.assertEqual(test1.__str__(), "[Rectangle] (1) 0/0 - 2/2")

        test2 = Rectangle(3, 2, 1, 1)
        self.assertEqual(test2.__str__(), "[Rectangle] (2) 1/1 - 3/2")

        test3 = Rectangle(3, 2, 1, 1, 12)
        self.assertEqual(test3.__str__(), "[Rectangle] (12) 1/1 - 3/2")

    def test_Rectangle_update(self):
        """ test for Rectangle_update """
        test1 = Rectangle(2, 2)
        test1.update(6, 8)
        self.assertEqual(test1.__str__(), "[Rectangle] (6) 0/0 - 8/2")

        with self.assertRaises(ValueError):
            test1.update(**{'width': 136, 'y': -2})
            test1.update(19, None, None)
        test1.update(None)
        self.assertEqual(test1.__str__(), "[Rectangle] (None) 0/0 - 136/2")

    def test_Rectangle_to_dictionary(self):
        """ test for Rectangle_to_dictionary function """
        test1 = Rectangle(2, 2)
        dir1 = {'id': 1, 'width': 2, 'height': 2, 'x': 0, 'y': 0}
        self.assertDictEqual(test1.to_dictionary(), dir1)

        test2 = Rectangle(2, 2, 7, 5, 12)
        dir2 = {'id': 12, 'width': 2, 'height': 2, 'x': 7, 'y': 5}
        self.assertDictEqual(test2.to_dictionary(), dir2)

    def test_display(self):
        """ test for display function """
        test1 = Rectangle(2, 2)
        f = StringIO()
        with redirect_stdout(f):
            test1.display()
            self.assertEqual(f.getvalue(), '##\n##\n')

        test2 = Rectangle(2, 2, 1, 1, 12)
        j = StringIO()
        with redirect_stdout(j):
            test2.display()
            self.assertEqual(j.getvalue(), '\n ##\n ##\n')


if __name__ == '__main__':
    unittest.main()
