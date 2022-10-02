#!/usr/bin/python3
"""Only sub class of"""


def inherits_from(obj, a_class):
    """function that returns True if the object is an instance of a class;
    otherwise False
    """
    if type(obj) != a_class:
        return isinstance(obj, a_class)
    return False
