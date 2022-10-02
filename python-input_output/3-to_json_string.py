#!/usr/bin/python3
"""To JSON string"""
import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string)
    """
    datastore = json.dumps(my_obj, sort_keys=True)
    return(datastore)
