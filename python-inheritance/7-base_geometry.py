#!/usr/bin/python3
"""Integer validator"""


class BaseGeometry:
    """Class Base"""

    def __dir__(self):
        """function __dir__ """
        obj = BaseGeometry
        return dir(obj)

    def area(self):
        """Method area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Method validator"""
        self.name = name
        self.value = value

        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(self.name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(self.name))
