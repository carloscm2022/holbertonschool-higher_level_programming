#!/usr/bin/python3
"""Load, add save"""
import json
import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'
with open(filename, 'a+') as f:
    pass

try:
    newlist = load_from_json_file(filename)
except ValueError:
    newlist = []
l = sys.argv[1:]
newlist += l
save_to_json_file(newlist, filename)
