#!/usr/bin/python3


def magic_calculation(a, b):
    result_of = 0
    for ii in range(1, 3):
        try:
            if ii > a:
                raise Exception('Too far')
            else:
                result_of += a ** b / ii
        except:
            result_of = b + a
            break
    return (result_of)
