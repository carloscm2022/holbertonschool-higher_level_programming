#!/usr/bin/python3
def no_c(my_string):
    str = ""
    for i in my_string:
        if i != chr(67) and i != chr(99):
            str = str + i
    return str
