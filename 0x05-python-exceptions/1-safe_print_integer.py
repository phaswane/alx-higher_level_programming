#!/usr/bin/python3

afe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except:
        return False
