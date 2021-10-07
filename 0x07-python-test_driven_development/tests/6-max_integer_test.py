#!/usr/bin/python3


import unittest
max_integer = __import__('6-max_integer').max_integer


class Test_max_integer(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_list_of_0(self):
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_module_docstring(self):
        """Check: module docsting"""
        module = __import__('6-max_integer').__doc__
        self.assertTrue(len(module) > 1)

    def test_function_docstring(self):
        """Check: function docstring"""
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)

    def test_tuple(self):
        self.assertEqual(max_integer((1, 2, 3, 4)), 4)

    def test_character_in_list(self):
        with self.assertRaises(TypeError):
            max_integer((1, 2, 3, 'a'))

    def test_inf_in_list(self):
        self.assertEqual(max_integer((1, 2, 3, float('inf'))), float('inf'))

    def test_none_in_list(self):
        with self.assertRaises(TypeError):
            max_integer((1, 2, 3, None))

    def test_empty_tuple(self):
        self.assertIsNone(max_integer(()))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1]), -1)

    def test_addition(self):
        self.assertEqual(max_integer([5 + 5, 3 * 2, 6 ** 3]), 216)

    def test_boolean(self):
        self.assertEqual(max_integer([True, False]), True)

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_string(self):
        self.assertEqual(max_integer("hola"), 'o')

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_matrix(self):
        self.assertEqual(max_integer([[1, 2], [2, 1], [3, 4]]), [3, 4])

    def test_huge_number(self):
        self.assertEqual(max_integer([126, 1e1010]), 1e1010)

    def test_tiny_number(self):
        self.assertEqual(max_integer([-126, 1e-1010]), 0.0)

    def test_hexadecimal(self):
        self.assertEqual(max_integer([0x09, 0x51, 0x08]), 0x51)
