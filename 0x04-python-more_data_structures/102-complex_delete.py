#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    _list = []
    for k, v in a_dictionary.items():
        if value is v:
            _list.append(k)
    if len(_list) > 0:
        for new in _list:
            del a_dictionary[new]
    return a_dictionary
