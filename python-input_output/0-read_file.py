#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """
    function that reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, 'r', encoding='utf8') as file:
        a = file.read()
        print(a, end='')
