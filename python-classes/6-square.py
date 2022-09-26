#!/usr/bin/python3
"""My first square"""


class Square:
    """Class define a square"""

    def __init__(self, size=0, position=(0, 0)):
        """init"""
        self.position = position
        self.size = size

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

    @property
    def position(self):
        """position"""
        return self.__position

    @position.setter
    def position(self, value):
        """position value"""
        if type(value) == tuple and len(value) == 2 and \
           type(value[0]) == int and type(value[1]) == int and \
           value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size is 0:
            print('')
        else:
            for i in range(self.__position[1]):
                print('')
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print('')
