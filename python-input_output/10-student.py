#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if type(attrs) is not list:
            return self.__dict__
        dict = {}

        for i in attrs:
            v = getattr(self, i, None)
            if v is not None:
                dict[i] = v
        return dict
