#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ tests for max_integer
    """

    def test_max_int(self):
        """ Basic example
        """
        test_list = [1, 2, 3, 8, 4]
        self.assertEqual(max_integer(test_list), 8)

    def test_max_empty(self):
        """ test if List is empty
        """
        self.assertEqual(max_integer([]), None)

    def test_max_alone(self):
        """ tests list with only one item
        """
        self.assertEqual(max_integer([1]), 1)

    def test_max_neg(self):
        """ tests list with negative int
        """
        test_list = [1, 2, 3, 8, 4, -40, -400, -12, 0]
        self.assertEqual(max_integer(test_list), 8)
