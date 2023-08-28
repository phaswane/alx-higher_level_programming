#!/usr/bin/python3

afe_print_list(my_list=[], x=0):
    _count = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
        except Exception as e:
            break
        else:
            _count += 1
    print()
    return _count
