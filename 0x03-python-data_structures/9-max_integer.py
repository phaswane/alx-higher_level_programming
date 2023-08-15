#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list:
        _imax = my_list[0]
        for i in my_list:
            if i > _imax:
                _imax = i
        return _imax

    return None
