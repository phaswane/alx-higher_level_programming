#!/usr/bin/python3

def no_c(my_string):
    _string = ""
    for c in my_string:
        if c not in "Cc":
            _string += c

    return _string
