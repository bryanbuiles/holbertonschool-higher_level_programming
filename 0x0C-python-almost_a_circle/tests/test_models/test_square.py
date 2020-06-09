#!/usr/bin/python3
"""Unittest for class Square
"""
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """unnitest
    Args:
        unittest: test for class Rectangle
    """

    def tearDown(self):
        """ tear module """
        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)

    def test_square_instances(self):
        """ test square_instances """
        test1 = Square(3)
        self.assertEqual(test1.id, 1)
        self.assertEqual(test1._Base__nb_objects, 1)

        test2 = Square(5, 0, 0, 7)
        self.assertEqual(test2.id, 7)
        self.assertEqual(test2._Base__nb_objects, 1)

        with self.assertRaises(TypeError):
            test3 = Square("bryan")
        with self.assertRaises(TypeError):
            tets4 = Square(None)
        with self.assertRaises(TypeError):
            test5 = Square(float("inf"))
        with self.assertRaises(TypeError):
            test6 = Square(5.5, 6.6)
        with self.assertRaises(TypeError):
            test8 = Square()
        with self.assertRaises(TypeError):
            test9 = Square(["hello"])
        with self.assertRaises(TypeError):
            test10 = Square({"hello": "bryan"})
        with self.assertRaises(TypeError):
            test11 = Square((1, 1))
        with self.assertRaises(TypeError):
            test12 = Square((1, 1, 1))
        with self.assertRaises(TypeError):
            test17 = Square(float('nan'))
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            test18 = Square("bryan", 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            test24 = Square(2, "bryan")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            test25 = Square(2, 5, "bryan")

        with self.assertRaises(ValueError):
            test13 = Square(5, -1)
        with self.assertRaises(ValueError):
            tets14 = Square(5, 1, -1)
        with self.assertRaises(ValueError):
            test15 = Square(5, -8)
        with self.assertRaises(ValueError):
            test16 = Square(-8, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            test19 = Square(-8)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            test20 = Square(5, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            tets21 = Square(5, 1, -1)

    def test_Square_area(self):
        """ test for Square area """
        test1 = Square(3)
        self.assertEqual(test1.area(), 9)

        test2 = Square(5, 0, 1, 7)
        self.assertEqual(test2.area(), 25)

    def test_Square_str(self):
        """ test for square str """
        test1 = Square(2)
        self.assertEqual(test1.__str__(), "[Square] (1) 0/0 - 2")

        test2 = Square(3, 1, 1)
        self.assertEqual(test2.__str__(), "[Square] (2) 1/1 - 3")

        test3 = Square(3, 1, 1, 12)
        self.assertEqual(test3.__str__(), "[Square] (12) 1/1 - 3")

    def test_Square_update(self):
        """ test for square """
        test1 = Square(2)
        test1.update(6, 8)
        self.assertEqual(test1.__str__(), "[Square] (6) 0/0 - 8")

        with self.assertRaises(ValueError):
            test1.update(**{'width': 137, 'y': -2})
            test1.update(19, x=8.5)

    def test_Square_to_dictionary(self):
        """ test for square_to_dictionary function """
        test1 = Square(2)
        dir1 = {'id': 1, 'size': 2, 'x': 0, 'y': 0}
        self.assertDictEqual(test1.to_dictionary(), dir1)

        test2 = Square(2, 7, 5, 12)
        dir2 = {'id': 12, 'size': 2, 'x': 7, 'y': 5}
        self.assertDictEqual(test2.to_dictionary(), dir2)

    def test_display(self):
        """ test for display function """
        test1 = Square(2)
        f = StringIO()
        with redirect_stdout(f):
            test1.display()
            self.assertEqual(f.getvalue(), '##\n##\n')

        test2 = Square(2, 1, 1, 12)
        j = StringIO()
        with redirect_stdout(j):
            test2.display()
            self.assertEqual(j.getvalue(), '\n ##\n ##\n')


if __name__ == '__main__':
    unittest.main()
