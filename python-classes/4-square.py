#!/usr/bin/python3
"""My firts square"""


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

    def area(self):
        """Instance that return current square area"""
        return self.__size * self.__size

    @property
    def size(self):
        """Retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """Use setter"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
