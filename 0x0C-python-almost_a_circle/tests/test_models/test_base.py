#!/usr/bin/python3


import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_base(unittest.TestCase):
    def test_base_case(self):
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_no_id_passed(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_create(self):
        dict1 = {"width": 5,
                 "height": 6,
                 "x": 1,
                 "y": 2,
                 "id": 3}
        b3 = Rectangle.create(**dict1)
        self.assertEqual(type(b3), Rectangle)
