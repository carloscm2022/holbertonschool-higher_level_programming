#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        val = list(a_dictionary.values())
        kes = list(a_dictionary.keys())
        return (kes[val.index(max(val))])
    return None
