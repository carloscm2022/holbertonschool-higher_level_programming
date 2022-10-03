#!/usr/bin/python3
"""This module named 7-add_item.py
   Created on Sunday, October 02, 2022
   @author: Daisy Chipana Lapa
"""


import json
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

len_arg = len(sys.argv)
filename = "add_item.json"
if not os.path.exists(filename):
    my_list = []
else:
    my_list = load_from_json_file(filename)
for i in range(1, len_arg):
    my_list.append(sys.argv[i])
save_to_json_file(my_list, filename)
