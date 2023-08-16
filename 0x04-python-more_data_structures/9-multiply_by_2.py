#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    _dict = a_dictionary.copy()
    for key in a_dictionary:
        _dict[key] *= 2
    return _dict
