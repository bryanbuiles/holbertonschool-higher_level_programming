#!/usr/bin/python3
"""Unittest for class Square
"""
import unittest
import os
import pep8
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Testing Square
    """

    def tearDown(self):
        """Tears down obj count
        """

        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_square_instances(self):
        """ test square_instances """

        test1 = Square(3)
        self.assertEqual(test1.id, 1)
        self.assertEqual(test1._Base__nb_objects, 1)

        test2 = Square(5, 0, 0, 7)
        self.assertEqual(test2.id, 7)
        self.assertEqual(test2._Base__nb_objects, 1)

        with self.assertRaises(ValueError):
            test1.width = -10

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

        with self.assertRaises(TypeError):
            test26 = Square(True, 1)

        with self.assertRaises(TypeError):
            test27 = Square()

        with self.assertRaises(TypeError):
            test28 = Square(1, 2, 3, 4, 5, 6, 4, 7, 8)

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

    def test_raises_y(self):
        """ test raises errors for y """

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            test3 = Square(1, 1, "bryan", 1)
        with self.assertRaises(TypeError):
            tets4 = Square(1, 1, None, 1)
        with self.assertRaises(TypeError):
            test5 = Square(1, 1, float("inf"), 1)
        with self.assertRaises(TypeError):
            test6 = Square(1, 1, 5.5, 6.6)
        with self.assertRaises(TypeError):
            test9 = Square(1, 1, ["hello"], 1)
        with self.assertRaises(TypeError):
            test10 = Square(1, 1, {"hello": "bryan"}, 1)
        with self.assertRaises(TypeError):
            test11 = Square(1, 1, (1, 1), 1)
        with self.assertRaises(TypeError):
            test12 = Square(1, 1, (1, 1, 1), 1)
        with self.assertRaises(TypeError):
            test17 = Square(1, 1, float('nan'), 1)
        with self.assertRaises(TypeError):
            test26 = Square(1, 1, True, 1)
        with self.assertRaises(TypeError):
            test27 = Square()
        with self.assertRaises(TypeError):
            test28 = Square(5, 2, 3, 4, 5, 4, 5, 4)

    def test_raises_x(self):
        """ test raises errors for x """

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            test3 = Square(1, "bryan", 1)
        with self.assertRaises(TypeError):
            tets4 = Square(1, None, 1)
        with self.assertRaises(TypeError):
            test5 = Square(1, float("inf"), 1)
        with self.assertRaises(TypeError):
            test6 = Square(1, 5.5, 6.6)
        with self.assertRaises(TypeError):
            test9 = Square(1, ["hello"], 1)
        with self.assertRaises(TypeError):
            test10 = Square(1, {"hello": "bryan"}, 1)
        with self.assertRaises(TypeError):
            test11 = Square(1, (1, 1), 1)
        with self.assertRaises(TypeError):
            test12 = Square(1, (1, 1, 1), 1)
        with self.assertRaises(TypeError):
            test17 = Square(1, float('nan'), 1)
        with self.assertRaises(TypeError):
            test26 = Square(1, True, 1)

    def test_Square_area(self):
        """ test for Square area """

        test1 = Square(3)
        self.assertEqual(test1.area(), 9)

        test2 = Square(5, 0, 1, 7)
        self.assertEqual(test2.area(), 25)

    def test_Square_str(self):
        """ test for square str """

        test1 = Square(2)
        test1.width = 3
        self.assertEqual(test1.__str__(), "[Square] (1) 0/0 - 3")

        test2 = Square(3, 1, 1)
        test2.x = 2
        self.assertEqual(test2.__str__(), "[Square] (2) 2/1 - 3")

        test3 = Square(3, 1, 1, 12)
        test3.y = 3
        self.assertEqual(test3.__str__(), "[Square] (12) 1/3 - 3")

    def test_Square_update(self):
        """ test for square """

        test1 = Square(2)
        test1.update(6, 8)
        self.assertEqual(test1.__str__(), "[Square] (6) 0/0 - 8")

        test2 = Square(2, 3, 4, 5)
        test2.update(**{'size': 136, 'y': 2})
        self.assertEqual(test2.__str__(), "[Square] (5) 3/2 - 136")

        test3 = Square(2, 3, 4, 6)
        test3.update(17, x=5)
        self.assertEqual(test3.__str__(), "[Square] (6) 5/4 - 2")

        with self.assertRaises(ValueError):
            test1.update(**{'width': 136, 'y': -2})
            test1.update(19, x=8.5)

    def test_Square_to_dictionary(self):
        """ test for square_to_dictionary function """

        test1 = Square(2)
        dir1 = {'id': 1, 'size': 2, 'x': 0, 'y': 0}
        self.assertEqual(test1.to_dictionary(), dir1)

        test2 = Square(2, 7, 5, 12)
        dir2 = {'id': 12, 'size': 2, 'x': 7, 'y': 5}
        self.assertEqual(test2.to_dictionary(), dir2)

    def test_display(self):
        """Testing display()
        """
        test1 = Square(2)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            test1.display()
            self.assertEqual(fakeOutput.getvalue(), '##\n##\n')
        test2 = Square(4, 0, 1, 12)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            test2.display()
            self.assertEqual(fakeOutput.getvalue(),
                             '\n####\n####\n####\n####\n')


if __name__ == '__main__':
    unittest.main()
