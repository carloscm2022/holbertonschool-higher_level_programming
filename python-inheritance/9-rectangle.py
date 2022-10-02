#!/usr/bin/python3
"""Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class son rectangle"""
    def __init__(self, width, height):
        """Constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """"Methodd area"""
        return (self.__width * self.__height)

    def __str__(self):
        """Method __str__"""
        return ('[Rectangle] {}/{}'.format(self.__width, self.__height))
