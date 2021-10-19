#!/usr/bin/python3

"""Module for test the rectangle class"""

import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
import os


class TestBaseClass(unittest.TestCase):
    def setUp(self):
        """Reset the number of objects"""
        Base.reset_nb_instances()

    def test_id(self):
        """Test valid id"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

    def test_id_valid_multiple(self):
        """Check multiple instances"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_id_valid_same_id(self):
        """Check if instances have the same id"""
        b6 = Base(77)
        self.assertEqual(b6.id, 77)
        b7 = Base(77)
        self.assertEqual(b7.id, 77)

    def test_id_valid_param_str(self):
        """Check str as id"""
        b8 = Base("Holberton")
        self.assertEqual(b8.id, "Holberton")

    def test_id_valid_param_list(self):
        """Check list as id"""
        b9 = Base([98, 977])
        self.assertEqual(b9.id, [98, 977])

    def test_id_valid_param_tuple(self):
        """Check tuple as id"""
        b10 = Base((98, 977))
        self.assertEqual(b10.id, (98, 977))

    def test_id_valid_param_dict(self):
        """Check dict as id"""
        b11 = Base({"98": 977})
        self.assertEqual(b11.id, {"98": 977})

    def test_id_valid_param_set(self):
        """Check set as id"""
        b12 = Base({"98", 977})
        self.assertEqual(b12.id, {"98", 977})

    def test_id_valid_param_float(self):
        """Check float as id"""
        b13 = Base(3.14)
        self.assertEqual(b13.id, 3.14)

    def test_id_valid_param_inf(self):
        """Check inf as id"""
        b14 = Base(float('inf'))
        self.assertEqual(b14.id, float('inf'))

    def test_id_valid_param_func(self):
        """Check inf as id"""
        b15 = Base(len)
        self.assertEqual(b15.id("Hi"), 2)

    def test_id_valid_isprivate(self):
        """Check whether __nb_objects is private"""
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

    def test_params_exceptions_args_six(self):
        """Checks wrong number of arguments, six"""
        with self.assertRaises(TypeError):
            r = Base(2, 3, 23, 12, 234, 4)

    def test_id(self):
        """Test valid id"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

    def test_ids(self):
        """Test valid ids"""
        r2 = Rectangle(32, 2)
        self.assertEqual(r2.id, 1)
        r3 = Rectangle(7, 2)
        self.assertEqual(r3.id, 2)
        r4 = Rectangle(32, 3, 0, 0, 77)
        self.assertEqual(r4.id, 77)

    def test_valid_parametrs(self):
        """Test with valid params"""
        r5 = Rectangle(3, 5, 2, 8, 108)
        self.assertEqual([r5.width, r5.height, r5.x, r5.y, r5.id],
                         [3, 5, 2, 8, 108])
        r6 = Rectangle(43, 23)
        self.assertEqual([r6.width, r6.height], [43, 23])

    def test_params_defaults(self):
        """Tests default values for x, y"""
        r7 = Rectangle(32, 12)
        self.assertEqual([r7.x, r7.y], [0, 0])

    def test_params_defaults_2(self):
        """Tests default params"""
        r8 = Rectangle(32, 32, 13)
        self.assertEqual([r8.width, r8.height, r8.x, r8.y, r8.id],
                         [32, 32, 13, 0, 1])

    def test_params_setters(self):
        """Check all setters"""
        r9 = Rectangle(32, 34)
        r9.width = 21
        self.assertEqual(r9.width, 21)
        r9.height = 87
        self.assertEqual(r9.height, 87)
        r9.x = 55
        self.assertEqual(r9.x, 55)
        r9.y = 444
        self.assertEqual(r9.y, 444)

    def test_params_exceptions_args(self):
        """Checks wrong number of arguments, zero"""
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_params_exceptions_args_one(self):
        """Checks wrong number of arguments, 1 args"""
        with self.assertRaises(TypeError):
            r = Rectangle(21)

    def test_params_exceptions_args_six(self):
        """Checks wrong number of arguments, six"""
        with self.assertRaises(TypeError):
            r = Rectangle(2, 3, 23, 12, 234, 4)

    def test_args_value_zero(self):
        """Check valid value"""
        msg = " must be > 0"
        err = ValueError
        try:
            Rectangle(-10, 10)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            Rectangle(10, -10)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)

        try:
            Rectangle(0, 10)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            Rectangle(10, 0)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)

        msg = " must be >= 0"
        try:
            Rectangle(10, 10, -2)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            Rectangle(10, 10, 2, -3)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_rectangle_value(self):
        """Test Rectangle"""
        with self.assertRaises(ValueError):
            Rectangle(32, 0)

    def test_params_str_width(self):
        """Check str as parameter"""
        with self.assertRaises(TypeError):
            Rectangle("string", 32)

    def test_params_str_height(self):
        """Check str as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(32, "string")

    def test_params_str_x(self):
        """Check str as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, "string")

    def test_params_str_y(self):
        """Check str as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, 321, "string")

    def test_params_str_width_err_msg(self):
        """Check str as parameter, error message"""
        try:
            Rectangle("string", 32)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_params_str_height_err_msg(self):
        """Check str as parameter, error message"""
        try:
            Rectangle(12, "String")
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_params_str_x_err_msg(self):
        """Check str as parameter, error message"""
        try:
            Rectangle(43, 32, "s")
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_params_str_y_err_msg(self):
        """Check str as parameter, error message"""
        try:
            Rectangle(43, 32, 3, "s")
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

    def test_params_list_width(self):
        """Check list as parameter"""
        with self.assertRaises(TypeError):
            Rectangle([21], 32)

    def test_params_list_height(self):
        """Check list as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(32, [32])

    def test_params_list_x(self):
        """Check list as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, [1])

    def test_params_list_y(self):
        """Check list as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, 321, [43])

    def test_params_list_width_err_msg(self):
        """Check list as parameter, error message"""
        try:
            Rectangle([234], 32)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_params_list_height_err_msg(self):
        """Check list as parameter, error message"""
        try:
            Rectangle(12, ["String"])
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_params_list_x_err_msg(self):
        """Check list as parameter, error message"""
        try:
            Rectangle(43, 32, ["s"])
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_params_list_y_err_msg(self):
        """Check list as parameter, error message"""
        try:
            Rectangle(43, 32, 3, ["s"])
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

    def test_params_tuple_width(self):
        """Check tuple as parameter"""
        with self.assertRaises(TypeError):
            Rectangle((21, 32), 32)

    def test_params_tuple_height(self):
        """Check tuple as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(32, (32, 443))

    def test_params_tuple_x(self):
        """Check tuple as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, (1, 54))

    def test_params_tuple_y(self):
        """Check tuple as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, 321, (43, 24))

    def test_params_tuple_width_err_msg(self):
        """Check tuple as parameter, error message"""
        try:
            Rectangle((234, 32), 32)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_params_tuple_height_err_msg(self):
        """Check tuple as parameter, error message"""
        try:
            Rectangle(12, ("String", 32))
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_params_tuple_x_err_msg(self):
        """Check tuple as parameter, error message"""
        try:
            Rectangle(43, 32, ("s", 4))
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_params_tuple_y_err_msg(self):
        """Check tuple as parameter, error message"""
        try:
            Rectangle(43, 32, 3, ("s", 542))
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

    def test_params_dict_width(self):
        """Check dict as parameter"""
        with self.assertRaises(TypeError):
            Rectangle({21: 32}, 32)

    def test_params_dict_height(self):
        """Check dict as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(32, {32: 443})

    def test_params_dict_x(self):
        """Check dict as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, {1: 54})

    def test_params_dict_y(self):
        """Check dict as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, 321, {43: 24})

    def test_params_dict_width_err_msg(self):
        """Check dict as parameter, error message"""
        try:
            Rectangle({234: 32}, 32)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_params_dict_height_err_msg(self):
        """Check dict as parameter, error message"""
        try:
            Rectangle(12, {"String": 32})
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_params_dict_x_err_msg(self):
        """Check dict as parameter, error message"""
        try:
            Rectangle(43, 32, {"s": 4})
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_params_dict_y_err_msg(self):
        """Check dict as parameter, error message"""
        try:
            Rectangle(43, 32, 3, {"s": 542})
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

    def test_params_none_width(self):
        """Check none as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(None, 32)

    def test_params_none_height(self):
        """Check none as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(32, None)

    def test_params_none_x(self):
        """Check none as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, None)

    def test_params_dict_none(self):
        """Check none as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, 321, None)

    def test_params_none_width_err_msg(self):
        """Check none as parameter, error message"""
        try:
            Rectangle(None, 32)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_params_none_height_err_msg(self):
        """Check none as parameter, error message"""
        try:
            Rectangle(12, None)
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_params_none_x_err_msg(self):
        """Check none as parameter, error message"""
        try:
            Rectangle(43, 32, None)
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_params_none_y_err_msg(self):
        """Check none as parameter, error message"""
        try:
            Rectangle(43, 32, 3, None)
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

    def test_params_set_width(self):
        """Check set as parameter"""
        with self.assertRaises(TypeError):
            Rectangle({21, 32}, 32)

    def test_params_set_height(self):
        """Check set as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(32, {32, 443})

    def test_params_set_x(self):
        """Check set as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, {1, 54})

    def test_params_set_y(self):
        """Check set as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, 321, {43, 24})

    def test_params_set_width_err_msg(self):
        """Check set as parameter, error message"""
        try:
            Rectangle({234, 32}, 32)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_params_set_height_err_msg(self):
        """Check set as parameter, error message"""
        try:
            Rectangle(12, {"String", 32})
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_params_set_x_err_msg(self):
        """Check set as parameter, error message"""
        try:
            Rectangle(43, 32, {"s", 4})
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_params_set_y_err_msg(self):
        """Check set as parameter, error message"""
        try:
            Rectangle(43, 32, 3, {"s": 542})
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

    def test_params_func_width(self):
        """Check function as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(len, 32)

    def test_params_func_height(self):
        """Check func as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(32, len)

    def test_params_func_x(self):
        """Check function as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, len)

    def test_params_func_y(self):
        """Check function as parameter"""
        with self.assertRaises(TypeError):
            Rectangle(12, 32, 321, len)

    def test_params_func_width_err_msg(self):
        """Check function as parameter, error message"""
        try:
            Rectangle(len, 32)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_params_func_height_err_msg(self):
        """Check function as parameter, error message"""
        try:
            Rectangle(12, len)
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_params_func_x_err_msg(self):
        """Check function as parameter, error message"""
        try:
            Rectangle(43, 32, len)
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_params_func_y_err_msg(self):
        """Check function as parameter, error message"""
        try:
            Rectangle(43, 32, 3, len)
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

    def test_area(self):
        """Simple area test"""
        r = Rectangle(32, 2)
        self.assertEqual(r.area(), 64)

    def test_exceptions(self):
        """Test exceptions"""
        with self.assertRaises(TypeError):
            s1 = Rectangle(10, 5)
            s1.area(32343)

    def test_00_case_width_success(self):
        new_obj = Rectangle(5, 10)
        self.assertEqual(new_obj.width, 5)

    def test_00_case_height_success(self):
        new_obj = Rectangle(5, 10)
        self.assertEqual(new_obj.height, 10)

    def test_00_case_x_default(self):
        new_obj = Rectangle(5, 10)
        self.assertEqual(new_obj.x, 0)

    def test_00_case_y_default(self):
        new_obj = Rectangle(5, 10)
        self.assertEqual(new_obj.y, 0)

    def test_00_case_id_default(self):
        new_obj = Rectangle(5, 10)
        self.assertEqual(new_obj.id, 1)

    def test_00_case_width_success_01(self):
        new_obj = Rectangle(8, 12, 5, 3, 26)
        self.assertEqual(new_obj.width, 8)

    def test_00_case_height_success_01(self):
        new_obj = Rectangle(8, 12, 5, 3, 26)
        self.assertEqual(new_obj.height, 12)

    def test_00_case_x_own(self):
        new_obj = Rectangle(8, 12, 5, 3, 26)
        self.assertEqual(new_obj.x, 5)

    def test_00_case_y_own(self):
        new_obj = Rectangle(8, 12, 5, 3, 26)
        self.assertEqual(new_obj.y, 3)

    def test_00_case_id_own(self):
        new_obj = Rectangle(8, 12, 5, 3, 26)
        self.assertEqual(new_obj.id, 26)

    def test_19_case_whitout_values(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_20_case_whit_just_one_value(self):
        with self.assertRaises(TypeError):
            Rectangle(2)

    def test_21_case_whit_more_than_one_value(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 3, 7, 8, 9, 10)

    def test_22_case_whit_float_values(self):
        with self.assertRaises(TypeError):
            Rectangle(3.8, 5.6, 7, 9)

    def test_23_case_whit_list(self):
        with self.assertRaises(TypeError):
            Rectangle([7, 9], 3)

    def test_24_case_check_area_result(self):
        new_obj = Rectangle(3, 2)
        self.assertEqual(new_obj.area(), 6)
        with self.assertRaises(TypeError):
            Rectangle.area()
        self.assertEqual(new_obj.area(), 6)
        with self.assertRaises(TypeError):
            Rectangle.area(3, 5, 6)
        self.assertEqual(new_obj.area(), 6)
        with self.assertRaises(TypeError):
            Rectangle.area(float('inf'), 5)

    def test_dimensions(self):
        """ check if w & h dimensions are validate """
        rDim = Rectangle(2, 8)
        self.assertEqual(rDim.width, 2)
        self.assertEqual(rDim.height, 8)
        rDim.width = 10
        rDim.height = 3
        self.assertEqual(rDim.width, 10)
        self.assertEqual(rDim.height, 3)
        rDim.width = 0x0F
        rDim.height = 0x0F
        self.assertEqual(rDim.width, 15)
        self.assertEqual(rDim.height, 15)
        self.assertRaises(TypeError, Rectangle, 'Cinco', 10)
        self.assertRaises(TypeError, Rectangle, 10, '5')
        self.assertRaises(TypeError, Rectangle, None, 10)
        self.assertRaises(TypeError, Rectangle, 10, None)
        self.assertRaises(TypeError, Rectangle, True, 10)
        self.assertRaises(TypeError, Rectangle, 10, True)
        self.assertRaises(ValueError, Rectangle, -5, 10)
        self.assertRaises(ValueError, Rectangle, 5, -10)
        self.assertRaises(ValueError, Rectangle, 10, 0)
        self.assertRaises(ValueError, Rectangle, 0, 10)

    def test_update_args(self):
        """ check the update function with 'no-keyword' arguments """
        rUpdateArg = Rectangle(1, 2)
        rUpdateArg.update(6)
        self.assertEqual(rUpdateArg.id, 6)
        rUpdateArg.update(10, 5)
        self.assertEqual(rUpdateArg.id, 10)
        self.assertEqual(rUpdateArg.area(), 5 * 2)
        rUpdateArg.update(10, 10, 10)
        self.assertEqual(rUpdateArg.area(), 10 * 10)
        rUpdateArg.update(10, 10, 10, 10)
        self.assertEqual(rUpdateArg.x, 10)
        rUpdateArg.update(10, 10, 10, 10, 10)
        self.assertEqual(rUpdateArg.y, 10)
        rUpdateArg.update(5, 10, 15, 20, 25)
        self.assertEqual(rUpdateArg.id, 5)
        self.assertEqual(rUpdateArg.area(), 10 * 15)
        self.assertEqual(rUpdateArg.x, 20)
        self.assertEqual(rUpdateArg.y, 25)
        rUpdateArg.update(5, 10, 15, 20, 25)
        self.assertEqual(rUpdateArg.id, 5)
        self.assertEqual(rUpdateArg.area(), 10 * 15)
        self.assertEqual(rUpdateArg.x, 20)
        self.assertEqual(rUpdateArg.y, 25)
        rUpdateArg.update('A', 10, 15, 20, 25)
        self.assertEqual(rUpdateArg.id, 'A')
        self.assertEqual(rUpdateArg.area(), 10 * 15)
        self.assertEqual(rUpdateArg.x, 20)
        self.assertEqual(rUpdateArg.y, 25)
        self.assertRaises(TypeError, rUpdateArg.update(), 6, "3", 10, 19, 14)
        self.assertRaises(TypeError, rUpdateArg.update(), 10, 5, 5, None, 0)
        with self.assertRaises(ValueError):
            rUpdateArg.update(10, 5, 0, 0, 0)

        with self.assertRaises(ValueError):
            rUpdateArg.update(10, 0, 5, 0, 0)

    def test_update_kwargs(self):
        """ check update function with 'key-worded' argument """
        rUpdateKarg = Rectangle(1, 2)
        rUpdateKarg.update(id=6)
        self.assertEqual(rUpdateKarg.id, 6)
        rUpdateKarg.update(id=10, width=5)
        self.assertEqual(rUpdateKarg.id, 10)
        self.assertEqual(rUpdateKarg.area(), 5 * 2)
        rUpdateKarg.update(id=10, width=7, height=8)
        self.assertEqual(rUpdateKarg.id, 10)
        self.assertEqual(rUpdateKarg.area(), 7 * 8)
        rUpdateKarg.update(id=10, width=7, height=8, x=9)
        self.assertEqual(rUpdateKarg.id, 10)
        self.assertEqual(rUpdateKarg.area(), 7 * 8)
        self.assertEqual(rUpdateKarg.x, 9)
        rUpdateKarg.update(y=14, height=10, id=6, x=19, width=3)
        self.assertEqual(rUpdateKarg.id, 6)
        self.assertEqual(rUpdateKarg.area(), 30)
        self.assertEqual(rUpdateKarg.x, 19)
        self.assertEqual(rUpdateKarg.y, 14)

    def test_01_case_instance_Square_success(self):
        new_obj1 = Square(5)
        self.assertIsInstance(new_obj1, Rectangle)

    def test_01_case_instance_fail_01(self):
        new_obj1 = {"size": 5}
        self.assertIsNot(new_obj1, (Rectangle, Square))

    def test_01_case_instance_fail_02(self):
        new_obj1 = {"width": 5, "height": 13}
        self.assertIsNot(new_obj1, (Rectangle, Square))

    def test_02_type_from_json_string_success(self):
        new_obj = Rectangle(2, 3)
        to_string = '[{"id": 1, "width": 10, "_Rectangle__height": 7, "_Rectangle__x": 2, "_Rectangle__y": 8}, {"id": 2, "_Rectangle__width": 2, "_Rectangle__height": 4, "_Rectangle__x": 0, "_Rectangle__y": 0}]'
        result = new_obj.from_json_string(to_string)
        self.assertEqual(type(result), list)

    def test_03_create_rquare_success(self):
        new_obj1 = Square(5)
        dictionary = {"size": 10}
        new_obj2 = new_obj1.create(**dictionary)
        self.assertIsInstance(new_obj2, Square)

    def test_03_create_rectangle_success(self):
        new_obj1 = Rectangle(5, 2)
        dictionary = {"width": 10, "height": 5, "x": 2, "y": 2}
        new_obj2 = new_obj1.create(**dictionary)
        self.assertIsInstance(new_obj2, Rectangle)

    def test_03_create_rquare_fail(self):
        new_obj1 = Square(5)
        dictionary = {"size": 10}
        new_obj2 = new_obj1.create(**dictionary)
        self.assertIsNot(new_obj2, Rectangle)

    def test_03_create_rectangle_fail(self):
        new_obj1 = Rectangle(5, 2)
        dictionary = {"width": 10, "height": 5, "x": 2, "y": 2}
        new_obj2 = new_obj1.create(**dictionary)
        self.assertIsNot(new_obj2, Square)

    def test_04_create_size_success(self):
        new_obj1 = Square(5)
        dictionary = {"size": 10}
        new_obj2 = new_obj1.create(**dictionary)
        self.assertEqual(new_obj2.size, 10)

    def test_04_create_x_success(self):
        new_obj1 = Square(5)
        dictionary = {"size": 10}
        new_obj2 = new_obj1.create(**dictionary)
        new_obj2.x = 15
        self.assertEqual(new_obj2.x, 15)

    def test_00_case_base_success(self):
        new_obj = Square(5)
        self.assertEqual(new_obj.size, 5)

    def test_00_case_all_args_success(self):
        new_obj = Square(15, 4, 7, 15)
        self.assertEqual(new_obj.x, 4)

    def test_00_case_all_args_fail(self):
        with self.assertRaises(TypeError):
            new_obj = Square(15, 4, "40", 15)

    def test_00_case_all_args_fail_negatives(self):
        with self.assertRaises(ValueError):
            new_obj = Square(-15, -5, -2, 8)

    def test_00_case_all_args_fail_zero(self):
        with self.assertRaises(ValueError):
            new_obj = Square(0, 0, 0, 8)

    def test_01_case_fail_01_without_args(self):
        with self.assertRaises(TypeError):
            new_obj = Square()

    def test_02_setter_size_height_success(self):
        new_obj = Square(8, 5, 3, 26)
        new_obj.size = 40
        self.assertEqual(new_obj.height, 40)

    def test_02_setter_size_width_success(self):
        new_obj = Square(8, 5, 3, 26)
        new_obj.size = 40
        self.assertEqual(new_obj.width, 40)

    def test_02_setter_size_fail(self):
        new_obj = Square(8, 5, 3, 26)
        with self.assertRaises(ValueError):
            new_obj.size = -8

    def test_02_setter_x_success(self):
        new_obj = Square(8, 5, 3, 26)
        new_obj.x = 40
        self.assertEqual(new_obj.x, 40)

    def test_args_valid_types_str(self):
        """Check valid types, str"""
        Base.reset_nb_instances
        r1 = Rectangle(10, 10, 10, 10)
        s = "string"
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_list(self):
        """Check valid types, list"""
        Base.reset_nb_instances
        r1 = Rectangle(10, 10, 10, 10)
        s = [32, 43]
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_set(self):
        """Check valid types, set"""
        Base.reset_nb_instances
        r1 = Rectangle(10, 10, 10, 10)
        s = {32, 43}
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_tuple(self):
        """Check valid types, tuple"""
        Base.reset_nb_instances
        r1 = Rectangle(10, 10, 10, 10)
        s = (32, 43)
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_dict(self):
        """Check valid types, dict"""
        Base.reset_nb_instances
        r1 = Rectangle(10, 10, 10, 10)
        s = {"Hi": 43}
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_float(self):
        """Check valid types, float"""
        Base.reset_nb_instances
        r1 = Rectangle(10, 10, 10, 10)
        s = 3.14
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_none(self):
        """Check valid types, dict"""
        Base.reset_nb_instances
        r1 = Rectangle(10, 10, 10, 10)
        s = None
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_value_zero(self):
        """Check valid value"""
        Base.reset_nb_instances
        r1 = Rectangle(10, 10, 10, 10)
        s = 0
        msg = " must be > 0"
        err = ValueError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        s = -1
        msg = " must be >= 0"
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_init_0(self):
        """Test init of Rectangle"""
        s1 = Square(5)
        st = "[Square] (1) 0/0 - 5"
        self.assertEqual(str(s1), st)

    def test_init_1(self):
        """Test init of Rectangle"""
        s1 = Square(5, 5)
        st = "[Square] (1) 5/0 - 5"
        self.assertEqual(str(s1), st)

    def test_attr_0(self):
        """Test attr of Rectangle"""
        s1 = Square(5)
        self.assertEqual([s1.width, s1.height], [5, 5])

    def test_attr_1(self):
        """Test attr of Rectangle, size should not created"""
        s1 = Square(2)
        with self.assertRaises(AttributeError):
            print(s1._Square__size)

    def test_attr_str(self):
        """Test attr of Square, size should not created"""
        with self.assertRaises(TypeError):
            Square("1")

        with self.assertRaises(TypeError):
            Square(1, "1")

        with self.assertRaises(TypeError):
            Square(1, 2, "1")

    def test_inheritence(self):
        """Tests if Square is child of Rectangle"""
        self.assertTrue(issubclass(Square, Rectangle))

    def test_exceptions(self):
        """Test exceptions"""
        with self.assertRaises(TypeError):
            s1 = Square(10, 2, 1, 32, 233232)

        with self.assertRaises(TypeError):
            s1 = Square()

    def test_attr_valuerr(self):
        """Test attr of Square"""
        with self.assertRaises(ValueError):
            Square(-1)

        with self.assertRaises(ValueError):
            Square(1, -1)

        with self.assertRaises(ValueError):
            Square(1, 2, -1)

        with self.assertRaises(ValueError):
            Square(0)

    def test_setter(self):
        """Checks setter"""
        s1 = Square(5)
        self.assertEqual(s1._Rectangle__width, 5)

    def test_getter(self):
        """Checks getter"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test_exceptions_0(self):
        """Test exceptions"""
        s1 = Square(5)
        msg = "width must be an integer"
        err = TypeError
        try:
            s1.size = "32322"
        except Exception as e:
            self.assertEqual(str(e), msg)
            self.assertTrue(isinstance(e, err))

    def test_exceptions_1(self):
        """Test exceptions"""
        s1 = Square(5)
        msg = "width must be > 0"
        err = ValueError
        try:
            s1.size = -32
        except Exception as e:
            self.assertEqual(str(e), msg)
            self.assertTrue(isinstance(e, err))

    def test_args_valid_types_str(self):
        """Check valid types, str"""
        Base.reset_nb_instances
        r1 = Rectangle(10, 10, 10, 10)
        s = "string"
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_list(self):
        """Check valid types, list"""
        Base.reset_nb_instances
        r1 = Rectangle(10, 10, 10, 10)
        s = [32, 43]
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_set(self):
        """Check valid types, set"""
        Base.reset_nb_instances
        r1 = Rectangle(10, 10, 10, 10)
        s = {32, 43}
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_tuple(self):
        """Check valid types, tuple"""
        Base.reset_nb_instances
        r1 = Rectangle(10, 10, 10, 10)
        s = (32, 43)
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_dict(self):
        """Check valid types, dict"""
        Base.reset_nb_instances
        r1 = Rectangle(10, 10, 10, 10)
        s = {"Hi": 43}
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_float(self):
        """Check valid types, float"""
        Base.reset_nb_instances
        r1 = Rectangle(10, 10, 10, 10)
        s = 3.14
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_none(self):
        """Check valid types, dict"""
        Base.reset_nb_instances
        r1 = Rectangle(10, 10, 10, 10)
        s = None
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_value_zero(self):
        """Check valid value"""
        Base.reset_nb_instances
        r1 = Rectangle(10, 10, 10, 10)
        s = 0
        msg = " must be > 0"
        err = ValueError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        s = -1
        msg = " must be >= 0"
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_setter(self):
        """Checks setter"""
        s1 = Square(5)
        self.assertEqual(s1._Rectangle__width, 5)

    def test_getter(self):
        """Checks getter"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test_exceptions_0(self):
        """Test exceptions"""
        s1 = Square(5)
        msg = "width must be an integer"
        err = TypeError
        try:
            s1.size = "32322"
        except Exception as e:
            self.assertEqual(str(e), msg)
            self.assertTrue(isinstance(e, err))

    def test_exceptions_1(self):
        """Test exceptions"""
        s1 = Square(5)
        msg = "width must be > 0"
        err = ValueError
        try:
            s1.size = -32
        except Exception as e:
            self.assertEqual(str(e), msg)
            self.assertTrue(isinstance(e, err))

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_to_json_string_rectangle_type(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_square_type(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dicts(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_save_to_file_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)

    def test_from_json_string_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_one_rectangle(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)

    def test_create_rectangle_original(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    def test_create_rectangle_new(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))

    def test_create_rectangle_is(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square_original(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))

    def test_create_square_new(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s2))

    def test_create_square_is(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_create_square_equals(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)

    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)

    


if __name__ == '__main__':
    unittest.main()
