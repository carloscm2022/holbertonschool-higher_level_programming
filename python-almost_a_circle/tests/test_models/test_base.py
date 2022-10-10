#!/usr/bin/python3

"""Unittest for class Base()"""

import unittest
from models.base import Base


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
