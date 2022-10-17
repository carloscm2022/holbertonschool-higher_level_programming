#!/usr/bin/python3
"""Unittest for class Base()
"""
import unittest
import io
import sys
import json
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    def test_Rectangle_arguments_exist(self):
        """This methods will be tested with all_arguments"""
        r1 = Rectangle(1, 2)
        self.assertEqual((r1.width, r1.height), (1, 2))

    def test_Rectangle_all_arguments(self):
        """This methods will be tested with all_arguments"""
        r1 = Rectangle(10, 2, 0, 0, 12)
        r2 = Rectangle(2, 10, 0, 0, 5)
        self.assertEqual(r1.id, 12)
        self.assertEqual(r2.id, 5)

    def test_Rectangle_two_arguments(self):
        """This methods will be tested with two_arguments"""
        r1 = Rectangle(13, 2)
        r2 = Rectangle(5, 4)
        r1.id = 1
        self.assertEqual(r1.id, 1)
        r2.id = 2
        self.assertEqual(r2.id, 2)


class Test_Rectangle_validate_atributes(unittest.TestCase):
    def test_Rectangle_str(self):
        """This methods will be tested with str value"""
        with self.assertRaises(TypeError):
            r1 = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            r2 = Rectangle(1, "2")

    def test_Rectangle_negative(self):
        """This methods will be tested with a negative number"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, -12)
        with self.assertRaises(ValueError):
            r2 = Rectangle(-11, 2)
        with self.assertRaises(ValueError):
            r3 = Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            r4 = Rectangle(1, 2, 3, -4)

    def test_Rectangle_zero(self):
        """This methods will be tested with a zero"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 0)
        with self.assertRaises(ValueError):
            r2 = Rectangle(0, 2)

    def test_Rectangle_if_x_str(self):
        """This methods will be tested with the atribute x as str"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 5, "2")
        with self.assertRaises(TypeError):
            r2 = Rectangle(5, 10, "3")

    def test_Rectangle_if_y_str(self):
        """This methods will be tested with the atribute y as str"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 5, 2, "2")
        with self.assertRaises(TypeError):
            r2 = Rectangle(5, 10, 3, "3")


class Test_Rectangle_Area_first(unittest.TestCase):
    def test_Rectangle_area_number_positive(self):
        """This methods will be tested with numbers positive"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r2.area(), 56)


class Test_Rectangle__str__exist(unittest.TestCase):
    def test_Rectangle_str__exist(self):
        """This methods will be tested in case of function __str__"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), '[Rectangle] (12) 2/1 - 4/6')


class Test_Rectangle_display(unittest.TestCase):
    def test_Rectangle_display_exist(self):
        """This methods will be tested in case if display exist"""
        output = io.StringIO()
        sys.stdout = output
        r1 = Rectangle(2, 3, 2, 2)
        r1.display()
        prints = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(output.getvalue(), prints)

    def test_Rectangle_display_exist_also_x(self):
        """This methods will be tested in case if display exist also x"""
        output = io.StringIO()
        sys.stdout = output
        r2 = Rectangle(3, 2, 1)
        r2.display()
        prints = " ###\n ###\n"
        self.assertEqual(output.getvalue(), prints)

    def test_Rectangle_display_if_not_exist_x_and_y(self):
        """This methods will be tested in case not exist value to x and y"""
        output = io.StringIO()
        sys.stdout = output
        r3 = Rectangle(3, 2)
        r3.display()
        prints = "###\n###\n"
        self.assertEqual(output.getvalue(), prints)


class Test_Rectangle_to_dictionary(unittest.TestCase):
    def test_Rectangle_to_dictionary(self):
        """This methods will be tested if Rectangle exist"""
        r10 = Rectangle(10, 2, 1, 9, 12)
        r1_dictionary = r10.to_dictionary()
        self.assertEqual(r1_dictionary['width'], 10)
        self.assertEqual(r1_dictionary['height'], 2)
        self.assertEqual(r1_dictionary['x'], 1)
        self.assertEqual(r1_dictionary['y'], 9)
        self.assertEqual(r1_dictionary['id'], 12)


class Test_Rectangle_update(unittest.TestCase):
    def test_Rectangle_update_args(self):
        """This methods will be tested with Update args"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.id = 1
        self.assertEqual(str(r1), '[Rectangle] (1) 10/10 - 10/10')
        r1.update(89)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 10/10')
        r1.update(89, 2)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 2/10')
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 2/3')
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), '[Rectangle] (89) 4/10 - 2/3')
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), '[Rectangle] (89) 4/5 - 2/3')

    def test_Rectangle_update_kwargs(self):
        """This methods will be tested with Update kwargs"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.id = 1
        r1.update(height=1)
        self.assertEqual(str(r1), '[Rectangle] (1) 10/10 - 10/1')
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), '[Rectangle] (1) 2/10 - 1/1')
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), '[Rectangle] (89) 3/1 - 2/1')
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), '[Rectangle] (89) 1/3 - 4/2')


class Test_Rectangle_create(unittest.TestCase):
    def test_Rectangle_create(self):
        """This methods will be tested with Create"""
        r1 = Rectangle.create(**{'id': 85})
        self.assertEqual(str(r1), '[Rectangle] (85) 0/0 - 1/1')

        r2 = Rectangle.create(**{'id': 85, 'width': 1})
        self.assertEqual(str(r2), '[Rectangle] (85) 0/0 - 1/1')

        r3 = Rectangle.create(**{'id': 85, 'width': 1, 'height': 2})
        self.assertEqual(str(r3), '[Rectangle] (85) 0/0 - 1/2')

        r4 = Rectangle.create(**{'id': 85, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(str(r4), '[Rectangle] (85) 3/0 - 1/2')

        r5 = Rectangle.create(**{'id': 85, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(str(r5), '[Rectangle] (85) 3/4 - 1/2')

        r6 = Rectangle(3, 5, 1)
        r6.id = 1
        r6_dictionary = r6.to_dictionary()
        r7 = Rectangle.create(**r6_dictionary)
        self.assertEqual(str(r7), '[Rectangle] (1) 1/0 - 3/5')


class Test_Rectangle_save_to_file(unittest.TestCase):
    def test_save_to_file(self):
        """This methods will be tested save_to_file"""
        test1 = Rectangle(1, 1, 1, 1)
        test2 = Rectangle(2, 2, 2, 2)
        lista = [test1, test2]
        Rectangle.save_to_file(lista)
        with open("Rectangle.json", "r") as file:
            ls = [test1.to_dictionary(), test2.to_dictionary()]
            self.assertEqual(json.dumps(ls), file.read())

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual('[]', file.read())

    def test_save_to_file_None(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            ls = []
            self.assertEqual(json.dumps(ls), file.read())


class Test_Rectangle_(unittest.TestCase):
    def test_load_from_none_file(self):
        """This methods will be tested None file"""
        Rectangle.save_to_file(None)
        recs = Rectangle.load_from_file()
        self.assertEqual(type(recs), list)
        self.assertEqual(len(recs), 0)

    def test_load_from_empty_file(self):
        """This methods will be tested empty file"""
        Rectangle.save_to_file([])
        recs = Rectangle.load_from_file()
        self.assertEqual(type(recs), list)
        self.assertEqual(len(recs), 0)
