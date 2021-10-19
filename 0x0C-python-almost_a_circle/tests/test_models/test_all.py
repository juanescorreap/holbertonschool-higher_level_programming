#!/usr/bin/python3


import unittest
import inspect
import json
import os
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_base(unittest.TestCase):
    def setUp(self):
        """Reset the number of objects"""
        Base.reset_nb_instances()

    def test_base_case(self):
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_no_id_passed(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_create(self):
        dict1 = {"width": 5,
                 "height": 6,
                 "x": 1,
                 "y": 2,
                 "id": 3}
        b1 = Rectangle.create(**dict1)
        self.assertEqual(type(b1), Rectangle)

    def test_00_base_case(self):
        """Test for a instance"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_01_base_cases(self):
        """Tests normal instances"""
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base()
        self.assertEqual(b2.id, 3)
        b3 = Base()
        self.assertEqual(b3.id, 4)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 5)

    def test_02_giving_not_a_integer(self):
        """Tests for None case"""
        b6 = Base()
        self.assertEqual(b6.id, 6)
        b7 = Base()
        self.assertEqual(b7.id, 7)
        b8 = Base()
        self.assertEqual(b8.id, 8)
        b9 = Base(None)
        self.assertEqual(b9.id, 9)

    def test_03_arguments_in_init(self):
        """Tests for arguments exceded in the class"""
        with self.assertRaises(TypeError):
            b10 = Base(1, 2)

    def test_04_infinite_passed(self):
        """Tests when infinite is passed to the class"""
        b11 = Base(float('inf'))
        self.assertEqual(b11.id, float('inf'))

    def test_negative_numbers(self):
        """Tests for negative numbers"""
        b12 = Base(-13)
        self.assertEqual(b12.id, -13)

    def test_floats_numbers(self):
        """Tests for floats numbers"""
        b13 = Base(13.3)
        self.assertEqual(b13.id, 13.3)

    def test_float_negative_numbers(self):
        """Tests for float negative numbers"""
        b14 = Base(-13.3)
        self.assertEqual(b14.id, -13.3)

    def test_bolean_true(self):
        """Tests for bloean true"""
        b15 = Base(True)
        self.assertEqual(b15.id, 1)

    def test_bolean_false(self):
        """Tests for bolean false numbers"""
        b16 = Base(False)
        self.assertEqual(b16.id, 0)

    def test_list_01(self):
        """Tests for list"""
        b17 = Base([])
        self.assertEqual(b17.id, [])

    def test_tuple_01(self):
        """Tests for tuple"""
        b18 = Base(())
        self.assertEqual(b18.id, ())

    def test_list_02(self):
        """Tests for list"""
        b19 = Base([1])
        self.assertEqual(b19.id, [1])

    def test_tuple_02(self):
        """Tests for list"""
        b20 = Base((1))
        self.assertEqual(b20.id, 1)

    def test_list_03(self):
        """Tests for list"""
        b21 = Base([1, 2, 3])
        self.assertEqual(b21.id, [1, 2, 3])

    def test_tuple_03(self):
        """Tests for tuple"""
        b22 = Base((1, 2, 3))
        self.assertEqual(b22.id, (1, 2, 3))

    def test_strings(self):
        """Tests for string"""
        b23 = Base("python")
        self.assertEqual(b23.id, "python")

    def test_character(self):
        """Tests for characters"""
        b24 = Base('C')
        self.assertEqual(b24.id, 'C')

    def test_05_instances_with_same_id(self):
        """Tests instances with same id"""
        b25 = Base(123)
        self.assertEqual(b25.id, 123)
        b26 = Base(123)
        self.assertEqual(b26.id, 123)

    def test_06_ids_too_large(self):
        """Tests id with long numbers"""
        b27 = Base(54651513215645416546546548974486846874987889877)
        self.assertEqual(
            b27.id, 54651513215645416546546548974486846874987889877)
        b28 = Base(
            87437568947689547689576985487689547569847654756486798954)
        self.assertEqual(
            b28.id, 87437568947689547689576985487689547569847654756486798954)

    def test_file(self):
        """test file"""
        file = "Rectangle.json"
        d = [{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7},
             {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open(file, "r") as file:
            self.assertEqual(json.loads(file.read()), d)

    def test_file_exists(self):
        """test file"""
        file = "Rectangle.json"
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.isfile(file))

    def test_file_overwrite(self):
        """test file"""
        file = "Rectangle.json"
        with open(file, "w") as f:
            f.write("Hi")
        d = [{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7},
             {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open(file, "r") as f:
            self.assertEqual(json.loads(f.read()), d)

    def test_file_s(self):
        """test file"""
        file = "Square.json"
        d = [{"y": 8, "x": 2, "id": 1, "size": 10},
             {"y": 0, "x": 0, "id": 2, "size": 2}]
        r1 = Square(10, 2, 8)
        r2 = Square(2)
        Square.save_to_file([r1, r2])

        with open(file, "r") as f:
            self.assertEqual(json.loads(f.read()), d)

    def test_file_exists_s(self):
        """test file"""
        file = "Square.json"
        r1 = Square(10, 2, 8)
        r2 = Square(2)
        Square.save_to_file([r1, r2])
        self.assertTrue(os.path.isfile(file))

    def test_file_overwrite_s(self):
        """test file"""
        file = "Square.json"
        with open(file, "w") as f:
            f.write("Hi")
        d = [{"y": 8, "x": 2, "id": 1, "size": 10},
             {"y": 0, "x": 0, "id": 2, "size": 2}]
        r1 = Square(10, 2, 8)
        r2 = Square(2)
        Square.save_to_file([r1, r2])

        with open(file, "r") as f:
            self.assertEqual(json.loads(f.read()), d)

    def test_exceptions(self):
        """Test Exceptions"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

        with self.assertRaises(TypeError):
            Rectangle.save_to_file(322, 323232)

        with self.assertRaises(TypeError):
            Square.save_to_file()

        with self.assertRaises(TypeError):
            Square.save_to_file(322, 323232)

    def test_empty(self):
        """Empty file"""
        filename = "Rectangle.json"
        if os.path.isfile(filename):
            os.remove(filename)
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        filename = "Square.json"
        if os.path.isfile(filename):
            os.remove(filename)

        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        filename = "Rectangle.json"
        if os.path.isfile(filename):
            os.remove(filename)

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        filename = "Square.json"
        if os.path.isfile(filename):
            os.remove(filename)

        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_classmethod(self):
        """Checks class method"""
        self.assertTrue(inspect.ismethod(Base.save_to_file))

    def test_notlist(self):
        """Checks not list type"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(32)

    def test_notlist_ofobjs(self):
        """Checks list of objs"""
        with self.assertRaises(AttributeError):
            Rectangle.save_to_file([32, 32])

    def test_convert(self):
        """Checks from_jon_string"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, list_input)

    def test_convert_empty(self):
        """Checks from_jon_string"""
        list_input = []
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)

    def test_exceptions(self):
        """Test exceptions"""
        with self.assertRaises(TypeError):
            Rectangle.from_json_string()

        with self.assertRaises(TypeError):
            Rectangle.from_json_string(32, 443)

        with self.assertRaises(TypeError):
            Square.from_json_string()

        with self.assertRaises(TypeError):
            Square.from_json_string(32, 443)

    def test_convert_empty_string(self):
        """Checks from_jon_string"""
        list_output = Rectangle.from_json_string("[]")
        self.assertEqual(list_output, [])

    def test_convert_return_(self):
        """Checks from_jon_string"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertTrue(isinstance(list_output, list))

    def test_create(self):
        """Test create"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 3/5")
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

        r1 = Square(3, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertEqual(str(r1), "[Square] (3) 1/0 - 3")
        self.assertEqual(str(r2), "[Square] (3) 1/0 - 3")
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_wrong(self):
        """Wrong number of args"""
        with self.assertRaises(TypeError):
            Rectangle.create("Hi")

        with self.assertRaises(TypeError):
            Square.create("Go")
        self.assertEqual(Base.create(), None)

    def test_classmethod(self):
        """Checks class method"""
        self.assertTrue(inspect.ismethod(Base.create))

    def test_exceptions(self):
        """Test exceptions"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        with self.assertRaises(TypeError):
            Rectangle.load_from_file(list_rectangles_input, 32, 3212)

        r1 = Square(10, 7, 2)
        r2 = Square(2)
        list_rectangles_input = [r1, r2]

        with self.assertRaises(TypeError):
            Square.load_from_file(list_rectangles_input, 32, 3212)

    def test_aaaaaa_no_file(self):
        """Test if there is no file"""
        file = "Rectangle.json"
        if os.path.isfile(file):
            os.remove(file)
        out = Rectangle.load_from_file()
        self.assertEqual(out, [])

        file = "Square.json"
        if os.path.isfile(file):
            os.remove(file)
        out = Square.load_from_file()
        self.assertEqual(out, [])

    def test_types(self):
        """"Test types"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_output = Rectangle.load_from_file()
        self.assertTrue(type(list_output))
        self.assertTrue(all(isinstance(i, Base) for i in list_output))

        r1 = Square(10, 7, 2)
        r2 = Square(2)
        list_rectangles_input = [r1, r2]
        Square.save_to_file(list_rectangles_input)
        list_output = Square.load_from_file()
        self.assertTrue(type(list_output))
        self.assertTrue(all(isinstance(i, Base) for i in list_output))

    def test_valid_data(self):
        """Simple test"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]

        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_classmethod(self):
        """Checks class method"""
        self.assertTrue(inspect.ismethod(Base.load_from_file))

    def test_00_base_case(self):
        """Tests for id"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        r4 = Rectangle(10, 2)
        self.assertEqual(r4.id, 3)

    def test_01_test_height_and_width(self):
        """Tests for height and width"""
        r5 = Rectangle(10, 2)
        self.assertEqual([r5.width, r5.height, r5.x, r5.y, r5.id],
                         [10, 2, 0, 0, 1])
        r6 = Rectangle(10, 2, 8, 9, 81)
        self.assertEqual([r6.width, r6.height, r6.x, r6.y, r6.id],
                         [10, 2, 8, 9, 81])
        r7 = Rectangle(44, 33)
        self.assertEqual([r7.width, r7.height], [44, 33])
        r8 = Rectangle(45, 43)
        self.assertEqual([r8.width, r8.height], [45, 43])

    def test_02_with_no_arguments(self):
        """Tests for no arguments"""
        with self.assertRaises(TypeError):
            r9 = Rectangle()
        with self.assertRaises(TypeError):
            r10 = Rectangle(32)

    def test_03_3_arguments(self):
        """Test with 3 arguments"""
        r11 = Rectangle(12, 13, 14)
        self.assertEqual([r11.width, r11.height, r11.x, r11.y, r11.id],
                         [12, 13, 14, 0, 1])

    def test_04_change_attributes_manually(self):
        """Tests changind manually the attributes"""
        r11 = Rectangle(45, 43)
        r11.width = 32
        r11.height = 11
        self.assertEqual([r11.width, r11.height], [32, 11])
        r12 = Rectangle(12, 13, 14, 15)
        r12.width = 22
        r12.height = 23
        r12.x = 24
        r12.y = 25
        self.assertEqual([r12.width, r12.height, r12.x, r12.y],
                         [22, 23, 24, 25])

    def test_00_base_case(self):
        """Checks the base cases"""
        try:
            r01 = Rectangle(10, "2")
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")
        try:
            r02 = Rectangle(10, 2)
            r02.width = -10
        except ValueError as e:
            self.assertEqual(str(e), "width must be > 0")
        try:
            r03 = Rectangle(10, 2)
            r03.x = {}
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")
        try:
            r04 = Rectangle(10, 2, 3, -1)
        except ValueError as e:
            self.assertEqual(str(e), "y must be >= 0")

    def test_01_string_argument_height(self):
        """Checks when height is string"""
        try:
            r1 = Rectangle(10, "2")
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_02_string_argument_witdh(self):
        """Checks when width is string"""
        try:
            r2 = Rectangle("10", 2)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_03_string_argument_x(self):
        """Checks when x is string"""
        try:
            r14 = Rectangle(10, 2, "str", 11)
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_04_string_argument_y(self):
        """Checks when y is string"""
        try:
            r15 = Rectangle(10, 2, 11, "str")
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

    def test_05_negative_argument_width(self):
        """Checks when width is a negative integer"""
        try:
            r3 = Rectangle(-10, 2)
        except ValueError as e:
            self.assertEqual(str(e), "width must be > 0")

    def test_06_negative_argument_height(self):
        """Checks when height is a negative integer"""
        try:
            r4 = Rectangle(10, -2)
        except ValueError as e:
            self.assertEqual(str(e), "height must be > 0")

    def test_07_negative_argument_x(self):
        """Checks when x is a negative integer"""
        try:
            r7 = Rectangle(10, 2, -1, 1)
        except ValueError as e:
            self.assertEqual(str(e), "x must be >= 0")

    def test_08_negative_argument_y(self):
        """Checks when y is a negative integer"""
        try:
            r8 = Rectangle(10, 2, 1, -1)
        except ValueError as e:
            self.assertEqual(str(e), "y must be >= 0")

    def test_09_zero_arguments_width(self):
        """Checks when width is 0"""
        try:
            r5 = Rectangle(0, 2)
        except ValueError as e:
            self.assertEqual(str(e), "width must be > 0")

    def test_10_zero_arguments_height(self):
        """Checks when height is 0"""
        try:
            r6 = Rectangle(10, 0)
        except ValueError as e:
            self.assertEqual(str(e), "height must be > 0")

    def test_11_zero_arguments_x_and_y(self):
        """Checks when x and y are 0"""
        r9 = Rectangle(10, 2, 0, 0)
        self.assertEqual([r9.width, r9.height, r9.x, r9.y],
                         [10, 2, 0, 0])

    def test_12_changing_x(self):
        """Checks when x is changed"""
        try:
            r10 = Rectangle(10, 2, 11, 11)
            r10.x = -11
        except ValueError as e:
            self.assertEqual(str(e), "x must be >= 0")

    def test_13_changing_y(self):
        """Checks when y is changed"""
        try:
            r11 = Rectangle(10, 2, 11, 11)
            r11.y = -11
        except ValueError as e:
            self.assertEqual(str(e), "y must be >= 0")

    def test_14_changing_width(self):
        """Checks when witdh is changed"""
        try:
            r12 = Rectangle(10, 2, 11, 11)
            r12.width = 0
        except ValueError as e:
            self.assertEqual(str(e), "width must be > 0")

    def test_15_changing_height(self):
        """Checks when height is changed"""
        try:
            r13 = Rectangle(10, 2, 11, 11)
            r13.height = 0
        except ValueError as e:
            self.assertEqual(str(e), "height must be > 0")

    def test_16_float_x(self):
        """Checks when x is float"""
        try:
            r16 = Rectangle(10, 2, 11.12, 11)
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_17_float_y(self):
        """Checks when y is float"""
        try:
            r17 = Rectangle(10, 2, 11, 11.12)
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

    def test_18_float_width(self):
        """Checks when width is float"""
        try:
            r30 = Rectangle(10.11, 2, 11, 11)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_19_float_height(self):
        """Checks when height is float"""
        try:
            r31 = Rectangle(10, 2.11, 11, 11)
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_20_list_x(self):
        """Checks when x is a list"""
        try:
            r22 = Rectangle(10, 2, [11], 11)
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_21_list_y(self):
        """Checks when y is a list"""
        try:
            r23 = Rectangle(10, 2, 11, [11])
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

    def test_22_list_x(self):
        """Checks when x is a list"""
        try:
            r24 = Rectangle(10, 2, [1, 2], 11)
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_23_list_y(self):
        """Checks when y is a list"""
        try:
            r25 = Rectangle(10, 2, 11, [1, 2])
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

    def test_24_list_width(self):
        """Checks when width is a list"""
        try:
            r32 = Rectangle([10], 2, 11, 11)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_25_list_height(self):
        """Checks when height is a list"""
        try:
            r33 = Rectangle(10, [2], 11, 11)
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_26_list_width(self):
        """Checks when width is a list"""
        try:
            r34 = Rectangle([10, 2], 2, 11, 11)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_27_list_height(self):
        """Checks when height is a list"""
        try:
            r35 = Rectangle(10, [2, 10], 11, 11)
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_28_tuple_x(self):
        """Checks when x is a tuple"""
        r26 = Rectangle(10, 2, (11), 11)
        self.assertEqual([r26.width, r26.height, r26.x, r26.y],
                         [10, 2, 11, 11])

    def test_29_tuple_y(self):
        """Checks when y is a tuple"""
        r27 = Rectangle(10, 2, 11, (11))
        self.assertEqual([r27.width, r27.height, r27.x, r27.y],
                         [10, 2, 11, 11])

    def test_30_tuple_x(self):
        """Checks when x is a tuple"""
        try:
            r28 = Rectangle(10, 2, (1, 2), 11)
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_31_tuple_y(self):
        """Checks when y is a tuple"""
        try:
            r29 = Rectangle(10, 2, 11, (1, 2))
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

    def test_32_tuple_width(self):
        """Checks when width is a tuple"""
        r36 = Rectangle((10), 2, 11, 11)
        self.assertEqual([r36.width, r36.height, r36.x, r36.y],
                         [10, 2, 11, 11])

    def test_33_tuple_height(self):
        """Checks when height is a tuple"""
        r37 = Rectangle(10, (2), 11, 11)
        self.assertEqual([r37.width, r37.height, r37.x, r37.y],
                         [10, 2, 11, 11])

    def test_34_tuple_width(self):
        """Checks when width is a tuple"""
        try:
            r38 = Rectangle((10, 2), 2, 11, 11)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_35_tuple_height(self):
        """Checks when height is a tuple"""
        try:
            r39 = Rectangle(10, (10, 2), 11, 11)
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_36_dictionary_height(self):
        """Checks when height is a tuple"""
        try:
            r40 = Rectangle(10, {10: 2}, 11, 11)
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_37_dictionary_width(self):
        """Checks when height is a dictionary"""
        try:
            r41 = Rectangle({10: 2}, 2, 11, 11)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_38_dictionary_x(self):
        """Checks when height is a dictionary"""
        try:
            r40 = Rectangle(10, 2, {10: 2}, 11)
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_39_dictionary_y(self):
        """Checks when x is a dictionary"""
        try:
            r41 = Rectangle(10, 2, 11, {10: 2})
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

    def test_40_infinite_width(self):
        """Checks when width is a dictionary"""
        try:
            r42 = Rectangle(float('inf'), 2, 11, 11)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_41_infinite_height(self):
        """Checks when height is a dictionary"""
        try:
            r43 = Rectangle(10, float('inf'), 11, 11)
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_42_infinite_x(self):
        """Checks when x is a dictionary"""
        try:
            r18 = Rectangle(10, 2, float('inf'), 11)
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_43_infinite_y(self):
        """Checks when y is a dictionary"""
        try:
            r19 = Rectangle(10, 2, 11, float('inf'))
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

    def test_45_not_a_number_width(self):
        """Checks when width is not a number"""
        try:
            Rectangle(float('nan'), 2)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_46_not_a_number_height(self):
        """Checks when height is not a number"""
        try:
            Rectangle(10, float('nan'))
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_46_not_a_number_x(self):
        """Check when x is not a number"""
        try:
            Rectangle(10, 2, float('nan'))
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_46_not_a_number_y(self):
        """Check when y is not a number"""
        try:
            Rectangle(10, 2, 11, float('nan'))
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

    def test_base_cases(self):
        """Tests for base cases"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_base_cases(self):
        """Tests when argumens is passed to area"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(3, 2)
            self.assertEqual(r1.area(2343456436), 6)

    def test_base_case_01(self):
        """Test for case base 01"""
        r1 = Rectangle(4, 6)
        self.assertEqual(r1.display(), None)

    def test_display(self):
        """Test display with valid arguments"""
        # creation of file that stores the
        # representation of display() in the future
        f = io.StringIO()
        s = ('#' * 4 + '\n') * 3
        r1 = Rectangle(4, 3)
        with redirect_stdout(f):
            # the result of display stores the content in
            # f accessing to his content with getvalue
            r1.display()
        # compare s and f
        self.assertEqual(f.getvalue(), s)

    def test_display_valid(self):
        """Test display with valid arguments"""
        file = io.StringIO()
        expected = ('#' * 32 + '\n') * 32
        r1 = Rectangle(32, 32)
        with redirect_stdout(file):
            r1.display()
        self.assertEqual(file.getvalue(), expected)

        file = io.StringIO()
        expected = ('#' * 2 + '\n') * 52
        r2 = Rectangle(2, 52)
        with redirect_stdout(file):
            r2.display()
        self.assertEqual(file.getvalue(), expected)
