""" A few functions that all provide the square root of a number """

def lazy_sqrt(x):
    """ simplest way to sqrt"""
    return x**0.5

def builtin_sqrt(x):
    """USes builtin"""
    from math import sqrt
    return sqrt(x)

def newton_sqrt(x):
    """uses the Newton method to return square root"""
    val = x
    while True:
        last = val
        val = (val + x /val) * 0.5
        if abs(val - last) < 1e-9:
            break
    return val