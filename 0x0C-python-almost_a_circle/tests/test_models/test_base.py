#!/usr/bin/python3
"""Unittest for class Base
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """unnitest
    Args:
        unittest: test for class Base
    """

    def tearDown(self):
        """ tear down """
        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)

    def test_base_instances(self):
        """ test instances """
        test1 = Base()
        test2 = Base(7)
        test3 = Base("bryan")
        test4 = Base({"bryan": "hola"})
        test5 = Base((5, 2))
        test6 = Base([1, "hello"])
        test7 = Base(None)
        test8 = Base(7.5)
        test9 = Base(float('inf'))
        test10 = Base(float('nan'))
        test11 = Base((1, 2))
        test12 = Base((1, 2, 3))
        test13 = Base(True)

        self.assertEqual(test1.id, 1)
        self.assertEqual(test2.id, 7)
        self.assertEqual(test7.id, 2)
        self.assertEqual(test3.id, "bryan")
        self.assertEqual(test4.id, {"bryan": "hola"})
        self.assertEqual(test5.id, (5, 2))
        self.assertEqual(test6.id, [1, "hello"])
        self.assertEqual(test8.id, 7.5)
        self.assertEqual(test9.id, float('inf'))
        self.assertTrue(test10.id != float('nan'))
        self.assertEqual(test11.id, (1, 2))
        self.assertEqual(test12.id, (1, 2, 3))
        self.assertEqual(test13.id, True)

    def test_to_json_string(self):
        """ test to_json_string function """
        test1 = [{"bryan": 1, "super": "hero"}]
        test2 = [{"bryan": 3}]
        test3 = None
        test4 = "string"
        test5 = 5897
        test6 = [[5, 4, 8]]
        test7 = []

        self.assertCountEqual(Base.to_json_string(test1),
                              '[{"bryan": 1, "super": "hero"}]')
        self.assertCountEqual(Base.to_json_string(test2), '[{"bryan": 3}]')
        self.assertCountEqual(Base.to_json_string(test3), '[]')
        self.assertCountEqual(Base.to_json_string(test4), '"string"')
        with self.assertRaises(TypeError):
            Base.to_json_string(test5)
        self.assertCountEqual(Base.to_json_string(test6), '[[5, 4, 8]]')
        self.assertCountEqual(Base.to_json_string(test7), '[]')
        self.assertEqual(len(Base.to_json_string(None)), 2)

    def test_from_json_string(self):
        """ test from_json_string function """
        test1 = [{"bryan": 1, "hero": "too"}]
        result1 = Base.to_json_string(test1)
        test2 = [{"bryan": 3}]
        result2 = Base.to_json_string(test2)
        test3 = None
        result3 = Base.to_json_string(test3)
        test4 = "string"
        result4 = Base.to_json_string(test4)
        test6 = [[5, 4, 8, 9]]
        result6 = Base.to_json_string(test6)
        test7 = []
        result7 = Base.to_json_string(test7)

        self.assertEqual(Base.from_json_string(result1), test1)
        self.assertEqual(Base.from_json_string(result2), test2)
        self.assertEqual(Base.from_json_string(result4), test4)
        self.assertEqual(Base.from_json_string(result6), test6)
        self.assertEqual(Base.from_json_string(result7), test7)
        self.assertEqual(Base.from_json_string(result3), [])
        self.assertEqual(Base.from_json_string(test1), [])
        self.assertEqual(Base.from_json_string(test3), [])
        self.assertEqual(Base.from_json_string(test7), [])
        self.assertEqual(len(Base.from_json_string(None)), 0)

    def test_create(self):
        """ test for create function """
        test1 = {'id': 2, 'width': 3, 'height': 2, 'x': 3, 'y': 5}
        result1 = Rectangle.create(**test1)
        self.assertEqual(result1.__str__(), '[Rectangle] (2) 3/5 - 3/2')

        test2 = {'id': 3, 'size': 4, 'x': 5, 'y': 7}
        resultsquare1 = Square.create(**test2)
        self.assertEqual(resultsquare1.__str__(), '[Square] (3) 5/7 - 4')

        test2 = {'id': 5, 'width': "bryan", 'height': 7, 'x': 8, 'y': 9}
        test3 = {'id': 1, 'size': "bryan", 'x': 3, 'y': 2}
        with self.assertRaises(TypeError):
            result2 = Rectangle.create(**test2)
        with self.assertRaises(TypeError):
            resultsquare2 = Square.create(**test3)

    def test_load_from_file(self):
        """ test for test_load_from_file """
        test1 = Rectangle(5, 2, 7, 7)
        test2 = Rectangle(3, 1, 5)
        test3 = Square(9, 5, 3)
        test4 = Square(8, 5)

        rectanglesave = Rectangle.save_to_file([test1, test2])
        squaresave = Square.save_to_file([test3, test4])

        rectangler = Rectangle.load_from_file()
        squarer = Square.load_from_file()

        self.assertEqual(rectangler[0].__str__(), '[Rectangle] (1) 7/7 - 5/2')
        self.assertEqual(rectangler[1].__str__(), '[Rectangle] (2) 5/0 - 3/1')
        self.assertEqual(squarer[0].__str__(), '[Square] (3) 5/3 - 9')
        self.assertEqual(squarer[1].__str__(), '[Square] (4) 5/0 - 8')

        self.assertIsInstance(rectangler[0], Rectangle)
        self.assertIsInstance(rectangler[1], Rectangle)

        self.assertIsInstance(squarer[0], Square)
        self.assertIsInstance(squarer[1], Square)

    def test_save_to_file(self):
        """ test for save_to_file function """
        test1 = Rectangle(5, 2, 7, 7)
        test2 = Rectangle(3, 1, 5)
        test3 = Square(9, 5, 3)
        test4 = Square(8, 5)

        rectanglesave = Rectangle.save_to_file([test1, test2])
        squaresave = Square.save_to_file([test3, test4])

        self.assertTrue(os.path.isfile('Rectangle.json'))
        self.assertTrue(os.path.isfile('Square.json'))


if __name__ == '__main__':
    unittest.main()
