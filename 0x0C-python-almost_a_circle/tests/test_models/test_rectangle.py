#!/usr/bin/python3
"""Unittest for class Rectangle
"""
import unittest
import os
import pep8
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Testing Rectangle
    """

    def tearDown(self):
        """Tears down obj count
        """
        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_rectangle_instances(self):
        """ test for rectnagle instances """
        test1 = Rectangle(3, 2)
        with self.assertRaises(ValueError):
            test1.width = -10
        self.assertEqual(test1.id, 1)
        self.assertEqual(test1._Base__nb_objects, 1)
        test2 = Rectangle(5, 2, 0, 0, 7)
        self.assertEqual(test2.id, 7)
        self.assertEqual(test2._Base__nb_objects, 1)

    def test_area(self):
        """Testing area()
        """
        o1 = Rectangle(3, 2)
        o2 = Rectangle(8, 7, 0, 0, 12)
        o3 = Rectangle(999, 999)
        self.assertEqual(o1.area(), 6)
        self.assertEqual(o2.area(), 56)
        self.assertEqual(o3.area(), 998001)

    def test_rectangle_raises_width(self):
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
        with self.assertRaises(TypeError):
            test26 = Rectangle(True, 1)
        with self.assertRaises(TypeError):
            test27 = Rectangle(1, 2, 3, 4, 35, 4, 5, 4)

    def test_raises_value(self):
        """ test for raises value """
        with self.assertRaises(ValueError):
            test13 = Rectangle(5, 2, -1)
        with self.assertRaises(ValueError):
            tets14 = Rectangle(5, 2, 1, -1)
        with self.assertRaises(ValueError):
            test15 = Rectangle(5, -8)
        with self.assertRaises(ValueError):
            test16 = Rectangle(-8, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            test19 = Rectangle(-8, 4)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            test20 = Rectangle(5, 2, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            tets21 = Rectangle(5, 2, 1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            test22 = Rectangle(5, -8)

    def test_raises_heigh(self):
        """ test raises errors for height """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            test3 = Rectangle(1, "bryan", 1)
        with self.assertRaises(TypeError):
            tets4 = Rectangle(1, None, 1)
        with self.assertRaises(TypeError):
            test5 = Rectangle(1, float("inf"), 1)
        with self.assertRaises(TypeError):
            test6 = Rectangle(1, 5.5, 6.6)
        with self.assertRaises(TypeError):
            test9 = Rectangle(1, ["hello"], 1)
        with self.assertRaises(TypeError):
            test10 = Rectangle(1, {"hello": "bryan"}, 1)
        with self.assertRaises(TypeError):
            test11 = Rectangle(1, (1, 1), 1)
        with self.assertRaises(TypeError):
            test12 = Rectangle(1, (1, 1, 1), 1)
        with self.assertRaises(TypeError):
            test17 = Rectangle(1, float('nan'), 1)
        with self.assertRaises(TypeError):
            test26 = Rectangle(1, True, 1)

    def test_raises_y(self):
        """ test raises errors for y """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            test3 = Rectangle(1, 1, 1, "bryan", 1)
        with self.assertRaises(TypeError):
            tets4 = Rectangle(1, 1, 1, None, 1)
        with self.assertRaises(TypeError):
            test5 = Rectangle(1, 1, 1, float("inf"), 1)
        with self.assertRaises(TypeError):
            test6 = Rectangle(1, 1, 1, 5.5, 6.6)
        with self.assertRaises(TypeError):
            test9 = Rectangle(1, 1, 1, ["hello"], 1)
        with self.assertRaises(TypeError):
            test10 = Rectangle(1, 1, 1, {"hello": "bryan"}, 1)
        with self.assertRaises(TypeError):
            test11 = Rectangle(1, 1, 1, (1, 1), 1)
        with self.assertRaises(TypeError):
            test12 = Rectangle(1, 1, 1, (1, 1, 1), 1)
        with self.assertRaises(TypeError):
            test17 = Rectangle(1, 1, 1, float('nan'), 1)
        with self.assertRaises(TypeError):
            test26 = Rectangle(1, 1, 1, True, 1)

    def test_raises_x(self):
        """ test raises errors for x """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            test3 = Rectangle(1, 1, "bryan", 1)
        with self.assertRaises(TypeError):
            tets4 = Rectangle(1, 1, None, 1)
        with self.assertRaises(TypeError):
            test5 = Rectangle(1, 1, float("inf"), 1)
        with self.assertRaises(TypeError):
            test6 = Rectangle(1, 1, 5.5, 6.6)
        with self.assertRaises(TypeError):
            test9 = Rectangle(1, 1, ["hello"], 1)
        with self.assertRaises(TypeError):
            test10 = Rectangle(1, 1, {"hello": "bryan"}, 1)
        with self.assertRaises(TypeError):
            test11 = Rectangle(1, 1, (1, 1), 1)
        with self.assertRaises(TypeError):
            test12 = Rectangle(1, 1, (1, 1, 1), 1)
        with self.assertRaises(TypeError):
            test17 = Rectangle(1, 1, float('nan'), 1)
        with self.assertRaises(TypeError):
            test26 = Rectangle(1, 1, True, 1)

    def test_display(self):
        """Testing display()
        """
        test1 = Rectangle(3, 2)
        with patch('sys.stdout', new=StringIO()) as f:
            test1.display()
            self.assertEqual(f.getvalue(), '###\n###\n')
        test2 = Rectangle(4, 5, 0, 1, 12)
        with patch('sys.stdout', new=StringIO()) as f:
            test2.display()
            self.assertEqual(f.getvalue(),
                             '\n####\n####\n####\n####\n####\n')

    def test_str(self):
        """Testing __str__()
        """
        test1 = Rectangle(3, 2)
        test2 = Rectangle(8, 7, 0, 0, 12)
        test3 = Rectangle(3, 2, 1)
        test4 = Rectangle(3, 2, id="bryan")
        self.assertEqual(test1.__str__(), '[Rectangle] (1) 0/0 - 3/2')
        self.assertEqual(test2.__str__(), '[Rectangle] (12) 0/0 - 8/7')
        self.assertEqual(test3.__str__(), '[Rectangle] (2) 1/0 - 3/2')
        self.assertEqual(test4.__str__(), '[Rectangle] (bryan) 0/0 - 3/2')

    def test_update(self):
        """Testing update()
        """
        test1 = Rectangle(3, 2)
        test2 = Rectangle(8, 7, 0, 0, 12)
        test4 = Rectangle(1, 2, id="bryan")
        test5 = Rectangle(5, 2, id="bryan")
        test1.update(5, 7)
        self.assertEqual(test1.__str__(), '[Rectangle] (5) 0/0 - 7/2')
        with self.assertRaises(ValueError):
            test2.update(**{'id': 1337, 'x': -1})
        test4.update(None)
        self.assertEqual(test4.__str__(), '[Rectangle] (None) 0/0 - 1/2')
        test5.update(-100)
        self.assertEqual(test5.__str__(), '[Rectangle] (-100) 0/0 - 5/2')

    def test_to_dictionary(self):
        """Testing to_dictionary()
        """
        test1 = Rectangle(2, 2)
        test2 = Rectangle(1, 2, 0, 0, 7)
        test3 = Rectangle(3, 2, 1, 4)
        test4 = Rectangle(3, 2, id="bryan")
        dirr1 = {'id': 1, 'width': 2, 'height': 2, 'x': 0, 'y': 0}
        dirr2 = {'id': 7, 'width': 1, 'height': 2, 'x': 0, 'y': 0}
        dirr3 = {'id': 2, 'width': 3, 'height': 2, 'x': 1, 'y': 4}
        dirr4 = {'id': 'bryan', 'width': 3, 'height': 2, 'x': 0, 'y': 0}
        self.assertDictEqual(test1.to_dictionary(), dirr1)
        self.assertDictEqual(test2.to_dictionary(), dirr2)
        self.assertDictEqual(test3.to_dictionary(), dirr3)
        self.assertDictEqual(test4.to_dictionary(), dirr4)


if __name__ == '__main__':
    unittest.main()
