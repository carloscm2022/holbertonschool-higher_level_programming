#!/usr/bin//python3
"""Class Base Unittest"""
import unittest
import io
import sys
from models.rectangle import Rectangle

class Test_Rectangle(unittest.TestCase):
	def test_Rectangle_arguments_exist(self):
		"""merhod will be tested with arguments"""
		r1 = Rectangle(1, 2)
		self.assertEqual((r1.width, r1.height), (1, 2))

	def test_Rectangle_all_arguments(self):
		"""proven methods with all_arguments"""
		r1 = Rectangle(11, 3, 0, 0, 13)
		r2 = Rectangle(3, 11, 0, 0, 6)
		self.assertEqual(r1.id, 13)
		self.assertEqual(r2.id, 6)

	def test_Rectangle_two_arguments(self:)
