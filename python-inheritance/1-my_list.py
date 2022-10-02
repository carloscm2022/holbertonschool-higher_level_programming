#!/usr/bin/python3
"""This module named 0-rectangle.py
   Created on Thursday, September 29, 2022
   @author: Daisy Chipana Lapa
"""


class MyList(list):
    """This class MyList that inherits from list
    Attributes:
       Nothing
    """
    def print_sorted(self):
        """Function named print_sorted
              Args:
                    self: class instance
              Returns:
                    Prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
