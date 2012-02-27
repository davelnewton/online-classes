def fmt(x):
    fmt = "%s"
    if type(x) == float:
        fmt = "%1.4f"
    elif type(x) == str:
        fmt = "  %s   "
    return fmt

def pp(arr):
    for s in [fmt(x) % x for x in arr]:
        print s,
    print

def pp2d(arrs):
    for yarr in arrs:
        pp(yarr)

def uniform_probability_2d(x, y):
    total = x * y
    p = 1.0 / total
    return [[p for i in range(0, x)] for j in range(0, y)]

R = "R"
G = "G"
world = [[R, R, R, R, R],
         [R, G, R, G, G],
         [R, G, R, G, R],
         [G, G, G, G, R],
         [G, G, R, R, R]]
p = uniform_probability_2d(5, 5)
pp2d(p)
