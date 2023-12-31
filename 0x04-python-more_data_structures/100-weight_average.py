#!/usr/bin/python3

def weight_average(my_list=[]):
    _weight = 0
    product = []
    if len(my_list) == 0:
        return 0
    for i in my_list:
        _weight += i[1]
        product.append(i[0] * i[1])
    return sum(product) / _weight
