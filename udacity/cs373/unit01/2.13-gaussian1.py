from math import *

def f(mu, sigma2, x):
    norm = 1 / sqrt(2.0 * pi * sigma2)
    expr = exp(-.5 * ((x - mu)**2 / sigma2))
    return norm * expr

print f(10., 4., 8.)
