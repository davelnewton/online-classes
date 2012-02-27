def fmt(x):
    fmt = "%s"
    if type(x) == float or type(x) == int:
        fmt = "%01.04f"
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

# Returns range of indexes for given array.
def idx(arr):
    return range(len(arr))

# Creates x by y array of zeroes.
def zeroes_2d(x, y):
    return [[0]*x for i in range(0, y)]
    
# Creates an x by y array with a 1 in given location.
def one_one(x, y, pos):
    q = zeroes_2d(x, y)
    q[pos[1]][pos[0]] = 1
    return q

def uniform_probability_2d(x, y):
    p = 1.0 / (x * y)
    return [[p for i in range(0, x)] for j in range(0, y)]

def sum_2d(p):
    return sum([sum(yarr) for yarr in p])

def normalize(p, s):
    return [n/s for n in p]

def normalize_2d(p):
    ret = []
    total = sum_2d(p)
    for yarr in p:
        ret.append(normalize(yarr, total))
    return ret

def sense(p, c, U):
    q = []
    for i, w in enumerate(c):
        mult = sensor_right if U == c[i] else sensor_wrong
        q.append(p[i] * mult)
    return q
    
def sense_2d(p, U):
    q = []
    for i in idx(p):
        #pp(p[i])
        #pp(colors[i])
        q.append(sense(p[i], colors[i], U))
    return normalize_2d(q)

def cidx_2d(a, x, y):
    ylen = len(a)
    xlen = len(a[0])
    return [x % xlen, y % ylen]

# Or itertools.permutations([-1, 0, 1], 2)
def offsets():
    q = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            q.append([i, j])
    return q

# Z will be array/tuple (x, y).
def move_2d(p, Z):
    q = zeroes_2d(len(p[0]), len(p))
    dx, dy = Z
    for y in idx(p):
        for x in idx(p[0]):
            pval = p[y][x]
            #print x, ",", y, "=", pval
            for ox, oy in offsets():
                mult = p_move if ((ox == 0) and (oy == 0)) else p_move_wrong
                #print cidx_2d(p, x+ox, y+oy), "=", mult*pval, " :: ",
                qx, qy = cidx_2d(p, x+dx+ox, y+dy+oy)
                q[qy][qx] += pval * mult
            #print
    return q

#
#
#

R, G = "red", "green"
measurements = [R, G]
motions = [[0, 0], [0, 1]]

sensor_right = 0.8 # Probability sensor is correct.
sensor_wrong = 1.0 - sensor_right

p_move = 1.0       # Probability move happens correctly.
p_move_wrong = 1.0 - p_move

colors = [[G, G, G],
          [G, R, R],
          [G, G, G]]
pp2d(colors)

p = uniform_probability_2d(3, 3)
pp2d(p)

pp2d(sense_2d(p, R))

move_2d(p, [1, 0])
