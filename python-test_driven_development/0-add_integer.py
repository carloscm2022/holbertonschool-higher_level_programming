#!/usr/bin/python3
"""
Function add
"""


def add_integer(a, b=98):
    """
    function that adds 2 integers.
    """
    if (type(a) is not (int)) and (type(a) is not (float)):
        raise TypeError('a must be an integer')
    elif type(b) is not (int) and (type(b) is not (float)):
        raise TypeError('b must be an integer')
    else:
        return int(a + b)
