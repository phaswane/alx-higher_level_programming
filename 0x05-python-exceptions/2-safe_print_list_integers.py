#!/usr/bin/python3

afe_print_list_integers(my_list=[], x=0):
    _count = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except IndexError:
            raise
        except:
            pass
        else:
            _count += 1
    print()
    return _count
