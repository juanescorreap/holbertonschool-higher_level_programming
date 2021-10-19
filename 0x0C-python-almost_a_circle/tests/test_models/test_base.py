#!/usr/bin/python3

"""Module for test the rectangle class"""

import unittest
from models.rectangle import Rectangle
from models.base import Base
import io


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


if __name__ == '__main__':
    unittest.main()



