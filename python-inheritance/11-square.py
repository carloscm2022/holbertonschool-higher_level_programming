#!/usr/bin/python3
"""This module named 10-square.py
   Created on Thursday, September 29, 2022
   @author: Daisy Chipana Lapa
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class Square
    Attributes:
       Nothing
    """
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return super().area()

    def __str__(self):
        return '[Square] {}/{}'.format(self.__size, self.__size)
