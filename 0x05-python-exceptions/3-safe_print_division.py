#!/usr/bin/python3

afe_print_division(a, b):
    try:
        _quotient = a / b
    except Exception as e:
        _quotient = None
    finally:
        print("Inside result: {}".format(_quotient))
    return _quotient
