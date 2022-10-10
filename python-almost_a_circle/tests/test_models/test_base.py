#!/usr/bin/python2
"""Unittest for class Base()"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Base(unittest.TestCase):
	def test_Base_id(self):
		"""Method that create a sequential id"""
		b1 = Base(15)
		b2 = Base(20)
		b3 = Base(4)

		self.assertEqual(b1.id, 15)
		self.assertEqual(b2.id, 20)
		self.assertEqual(b3.id, 4)

	def test_Base_empty(self):
		"""Method id empty"""
		b1 = Base()
		self.assertEqual(b1.id, 1)

	def test_Base_Negative(self):
		"""Method id negative"""
		b1 = Base(-15)
		b2 = Base(-20)
		b3 = Base(-4)

		self.assertEqual(b1.id, -15)
		self.assertEqual(b2.id, -20)
		self.assertEqual(b3.id, -4)

	def test_Base_to_json_string_None(self):
		"""Method validates a parameter empty"""
		json_dictionary = Base.to_json_string(None)
		self.assertEqual(json_dictionary, '[]')

	def test_Base_to_json_string_empty(self):
		"""Method validates a parameter empty"""
		json_dictionary = Base.to_json_string([])
		self.assertEqual(json_dictionary, '[]')

	def test_Base_to_json_string_exist(self):
		"""Methods validates a parameter exist"""
		dictionary = {'x': 3, 'width': 16, 'id': 1, 'height': 9, 'y': 10}
		json_dictionary = Base.to_json_string([dictionary])
		self.assertEqual(json_dictionary, '[{"x": 3, "width": 16, "id": 1, "height": 9, "y": 10}]')

	def test_Base_from_json_string_None(self):
		"""methods from_json_string validates a parameter None"""
		list_output = Rectangle.from_json_string(None)
		self.assertEqual(list_output, [])

	def test_Base_from_json_string_Empty(self):
		"""This methods from_json_string validates a parameter Empty"""
		list_output = Rectangle.from_json_string('[]')
		self.assertEqual(list_output, [])
	def test_Base_from_json_string_exist(self):
		"""method from_json_string validates a parameter Exist"""
		list_output = Rectangle.from_json_string('[{"height": 5, "width": 11, "id": 90}, {"height": 8, "width": 2, "id": 9}]')
		self.assertEqual(list_output, [{'height': 5, 'width': 11, 'id': 90}, {'height': 8, 'width': 2, 'id': 9}])
