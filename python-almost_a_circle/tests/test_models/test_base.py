#!/usr/bin/python3
"""Unittest for class Base()
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Base(unittest.TestCase):
    def test_Base_Id(self):
        """This methods create a id secuential"""
        b1 = Base(5)
        b2 = Base(12)
        self.assertEqual(b1.id, 5)
        self.assertEqual(b2.id, 12)

    def test_Base_Empty(self):
        """This methods create a id Empty"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_Base_Negative(self):
        """This methods create a id Negative"""
        b1 = Base(-5)
        b2 = Base(-13)
        self.assertEqual(b1.id, -5)
        self.assertEqual(b2.id, -13)

    def test_Base_to_json_string_None(self):
        """This methods validates a parameter None"""
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, '[]')

    def test_Base_to_json_string_empty(self):
        """This methods validates a parameter Empty"""
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, '[]')

    def test_Base_to_json_string_exist(self):
        """This methods validates a parameter Exist"""
        dictionary = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')

    def test_Base_from_json_string_None(self):
        """This methods from_json_string validates a parameter None"""
        list_output = Rectangle.from_json_string(None)
        self.assertEqual(list_output, [])

    def test_Base_from_json_string_Empty(self):
        """This methods from_json_string validates a parameter Empty"""
        list_output = Rectangle.from_json_string([])
        self.assertEqual(list_output, [])

    def test_Base_from_json_string_exist(self):
        """This methods from_json_string validates a parameter Exist"""
        list_output = Rectangle.from_json_string('[{"height": 4, "width": 10, "id": 89}, {"height": 7, "width": 1, "id": 7}]')
        self.assertEqual(list_output, [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}])
