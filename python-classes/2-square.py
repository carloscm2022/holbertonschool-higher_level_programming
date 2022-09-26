#!/usr/bin/python3
"""My first square"""


class Square:
    """Class define a square"""
    __size = ''

    def __init__(self, size=0):
        """init"""
        self.__size = size
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
