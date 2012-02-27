def fmt(x):
    fmt = "%s"
    if type(x) == float:
        fmt = "%1.4f"
    elif type(x) == str:
        fmt = "%6s"
    return fmt

def pp(arr):
    for s in [fmt(x) % x for x in arr]:
        print s,
    print

def pp2d(arrs):
    for yarr in arrs:
        pp(yarr)

def sum_2d(p):
    return sum([sum(yarr) for yarr in p])

def uniform_probability_2d(x, y):
    total = x * y
    p = 1.0 / total
    return [[p for i in range(0, x)] for j in range(0, y)]

#
#
#

measurements = ['red']
motions = [[0, 0]]

sensor_right = 1.0 # Probability sensor is correct.
p_move = 1.0       # Probability move happens correctly.

R, G = "red", "green"
colors = [[G, G, G],
          [G, R, G],
          [G, G, G]]
pp2d(colors)

p = uniform_probability_2d(3, 3)
pp2d(p)

