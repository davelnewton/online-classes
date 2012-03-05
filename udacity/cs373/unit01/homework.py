def fmt(x):
    f = "%s"
    if (type(x) == float) or (type(x) == int):
        f = "%01.04f"
    elif (type(x) == str):
        f = "%6s"
    return f

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
def z2d(x, y):
    return [[0]*x for i in range(0, y)]

# Uniform probability matrix given n positions.
def u2dn(x, y, positions):
    vu = 1.0 / len(positions)
    q = z2d(x, y)
    for x, y in positions:
        q[y][x] = vu
    return q
    
def u2d(x, y):
    p = 1.0 / (x * y)
    return [[p for i in range(0, x)] for j in range(0, y)]

def sum2d(p):
    return sum([sum(yarr) for yarr in p])

def N(p, s):
    return [n/s for n in p]

def N2d(p):
    ret = []
    total = sum2d(p)
    for yarr in p:
        ret.append(N(yarr, total))
    return ret

def S(p, c, U):
    q = []
    for i, w in enumerate(c):
        mult = sensor_right if U == c[i] else sensor_wrong
        q.append(p[i] * mult)
    return q
    
def S2d(p, U):
    q = []
    for i in idx(p):
        #pp(p[i])
        #pp(colors[i])
        q.append(S(p[i], colors[i], U))
    return N2d(q)

def cidx_2d(a, x, y):
    ylen = len(a)
    xlen = len(a[0])
    return swap([x % xlen, y % ylen])

# Or itertools.permutations([-1, 0, 1], 2)
def offsets():
    q = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            q.append([i, j])
    return q

def swap(a):
    return [a[1], a[0]]

# Z will be array/tuple (x, y).
def M2d(p, Z):
    q = z2d(len(p[0]), len(p))
    dy, dx = Z
    for y in idx(p):
        for x in idx(p[0]):
            pval = p[y][x]
            mult = p_move
            n = pval * mult
            qx, qy = cidx_2d(p, x+dx, y+dy)
            q[qy][qx] += n

            mult = p_move_wrong
            n = pval * mult
            qx, qy = cidx_2d(p, x, y)
            q[qy][qx] += n
    return N2d(q)

def MS2d(p, Zs, Us):
    q = p
    for i in idx(Zs):
        q = M2d(q, Zs[i])
        q = S2d(q, Us[i])
    return q

#
#
#

R, G = "red", "green"

sensor_right = 1.0 # Probability sensor is correct.
sensor_wrong = 1.0 - sensor_right

p_move = 1.0       # Probability move happens correctly.
p_move_wrong = 1.0 - p_move

#
# Test 1
#
sensor_right = 1.0 # Probability sensor is correct.
sensor_wrong = 1.0 - sensor_right

p_move = 1.0       # Probability move happens correctly.
p_move_wrong = 1.0 - p_move

colors = [[G, G, G],
          [G, R, G],
          [G, G, G]]
pp2d(colors)
p = u2d(3, 3)
pp2d(p)

p1 = M2d(p, [0, 0])
pp2d(p1)
p2 = S2d(p1, R)
pp2d(p2)

#
# Test 2
#

colors = [[G, G, G],
          [G, R, R],
          [G, G, G]]
pp2d(colors)
p = u2d(3, 3)
pp2d(p)

p1 = M2d(p, [0, 0])
pp2d(p1)
p2 = S2d(p1, R)
pp2d(p2)

#
# Test 3
#

sensor_right = 0.8 # Probability sensor is correct.
sensor_wrong = 1.0 - sensor_right

pp2d(colors)
p = u2d(3, 3)
pp2d(p)

p1m = M2d(p, [0, 0])
pp2d(p1m)
p1s = S2d(p1m, R)
pp2d(p1s)

#
# Test 4
#

pp2d(colors)
p = u2d(3, 3)
pp2d(p)

p1m = M2d(p, [0, 0])
pp2d(p1m)
p1s = S2d(p1m, R)
pp2d(p1s)
p = p1s

p2m = M2d(p, [0, 1])
pp2d(p2m)
p2s = S2d(p2m, R)
pp2d(p2s)

#
# Test 5
#

sensor_right = 1.0 # Probability sensor is correct.
sensor_wrong = 1.0 - sensor_right

pp2d(colors)
p = u2d(3, 3)
pp2d(p)

p1m = M2d(p, [0, 0])
pp2d(p1m)
p1s = S2d(p1m, R)
pp2d(p1s)
p = p1s

p2m = M2d(p, [0, 1])
pp2d(p2m)
p2s = S2d(p2m, R)
pp2d(p2s)

#
# Test 6
#

sensor_right = 0.8 # Probability sensor is correct.
sensor_wrong = 1.0 - sensor_right

p_move = 1.0       # Probability move happens correctly.
p_move_wrong = 1.0 - p_move

pp2d(colors)
p = u2d(3, 3)
pp2d(p)

p1m = M2d(p, [0, 0])
pp2d(p1m)
p1s = S2d(p1m, R)
pp2d(p1s)

p2m = M2d(p1s, [0, 1])
pp2d(p2m)
p2s = S2d(p2m, R)
pp2d(p2s)

#
#
#

sensor_right = 0.8 # Probability sensor is correct.
sensor_wrong = 1.0 - sensor_right

p_move = 0.5       # Probability move happens correctly.
p_move_wrong = 1.0 - p_move

pp2d(colors)
p = u2d(3, 3)
pp2d(p)

p1m = M2d(p, [0, 0])
pp2d(p1m)
p1s = S2d(p1m, R)
pp2d(p1s)

p2m = M2d(p1s, [0, 1])
pp2d(p2m)
p2s = S2d(p2m, R)
pp2d(p2s)

#
#
#

measurements = [R, R]
motions = [[0, 0], [0, 1]]

sensor_right = 1.0 # Probability sensor is correct.
sensor_wrong = 1.0 - sensor_right

p_move = 0.5       # Probability move happens correctly.
p_move_wrong = 1.0 - p_move

q = MS2d(p, motions, measurements)
pp2d(q)

#
#
#

colors = [[R, G, G, R, R],
          [R, R, G, R, R],
          [R, R, G, G, R],
          [R, R, R, R, R]]
measurements = [G, G, G, G, G]
motions = [[0, 0], [0, 1], [1, 0], [1, 0], [0, 1]]

sensor_right = 0.7 # Probability sensor is correct.
sensor_wrong = 1.0 - sensor_right

p_move = 0.8       # Probability move happens correctly.
p_move_wrong = 1.0 - p_move

p = u2d(5, 4)
q = MS2d(p, motions, measurements)
pp2d(q)
